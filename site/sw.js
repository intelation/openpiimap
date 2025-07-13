// OpenPIIMap Service Worker - Offline Capabilities
// Version 1.0.0

const CACHE_NAME = 'openpiimap-v1';
const STATIC_CACHE_NAME = 'openpiimap-static-v1';
const DATA_CACHE_NAME = 'openpiimap-data-v1';

// Assets to cache immediately
const STATIC_ASSETS = [
    './',
    './index.html',
    './map.html',
    './compare.html',
    './dashboard.html',
    './api.html',
    './integration.html',
    './assets/css/style.css',
    './assets/js/main.js',
    './json/countries.json',
    './json/frameworks.json',
    // Bootstrap and other CDN assets
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.css',
    'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap',
    // Leaflet
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
    // Chart.js
    'https://cdn.jsdelivr.net/npm/chart.js',
    // Prism.js
    'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css',
    'https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js'
];

// API endpoints to cache
const API_ENDPOINTS = [
    './json/',
    './countries/'
];

// Install event - cache static assets
self.addEventListener('install', event => {
    console.log('Service Worker: Installing...');
    
    event.waitUntil(
        Promise.all([
            // Cache static assets
            caches.open(STATIC_CACHE_NAME).then(cache => {
                console.log('Service Worker: Caching static assets');
                return cache.addAll(STATIC_ASSETS.map(url => {
                    return new Request(url, { mode: 'cors' });
                }));
            }),
            
            // Cache critical data
            cacheInitialData()
        ]).then(() => {
            console.log('Service Worker: Installation complete');
            return self.skipWaiting();
        }).catch(error => {
            console.error('Service Worker: Installation failed', error);
        })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
    console.log('Service Worker: Activating...');
    
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    // Delete old cache versions
                    if (cacheName !== STATIC_CACHE_NAME && 
                        cacheName !== DATA_CACHE_NAME &&
                        cacheName.startsWith('openpiimap-')) {
                        console.log('Service Worker: Deleting old cache', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            console.log('Service Worker: Activation complete');
            return self.clients.claim();
        })
    );
});

// Fetch event - serve from cache with network fallback
self.addEventListener('fetch', event => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Handle different types of requests
    if (request.method === 'GET') {
        if (isStaticAsset(request)) {
            // Static assets - cache first strategy
            event.respondWith(cacheFirst(request));
        } else if (isAPIRequest(request)) {
            // API requests - network first with cache fallback
            event.respondWith(networkFirstWithCache(request));
        } else if (isPageRequest(request)) {
            // HTML pages - network first with offline fallback
            event.respondWith(networkFirstWithOfflinePage(request));
        } else {
            // Other requests - network only
            event.respondWith(fetch(request));
        }
    }
});

// Message event - handle cache updates from main thread
self.addEventListener('message', event => {
    const { type, data } = event.data;
    
    switch (type) {
        case 'CACHE_COUNTRY_DATA':
            cacheCountryData(data);
            break;
            
        case 'CACHE_SEARCH_RESULTS':
            cacheSearchResults(data);
            break;
            
        case 'CLEAR_CACHE':
            clearAllCaches();
            break;
            
        case 'GET_CACHE_STATUS':
            getCacheStatus().then(status => {
                event.ports[0].postMessage(status);
            });
            break;
            
        case 'SYNC_DATA':
            syncDataInBackground();
            break;
    }
});

// Background sync event
self.addEventListener('sync', event => {
    if (event.tag === 'background-sync') {
        event.waitUntil(syncDataInBackground());
    }
});

// Helper functions

function isStaticAsset(request) {
    const url = new URL(request.url);
    return url.pathname.includes('/assets/') ||
           url.pathname.endsWith('.css') ||
           url.pathname.endsWith('.js') ||
           url.pathname.endsWith('.png') ||
           url.pathname.endsWith('.jpg') ||
           url.pathname.endsWith('.svg') ||
           url.hostname.includes('cdn.jsdelivr.net') ||
           url.hostname.includes('unpkg.com') ||
           url.hostname.includes('fonts.googleapis.com') ||
           url.hostname.includes('fonts.gstatic.com');
}

function isAPIRequest(request) {
    const url = new URL(request.url);
    return url.pathname.startsWith('/json/') ||
           url.pathname.startsWith('/api/') ||
           (url.hostname === 'api.openpiimap.org');
}

function isPageRequest(request) {
    const url = new URL(request.url);
    return request.headers.get('accept')?.includes('text/html') ||
           url.pathname.endsWith('.html') ||
           url.pathname === '/';
}

async function cacheFirst(request) {
    try {
        const cache = await caches.open(STATIC_CACHE_NAME);
        const cachedResponse = await cache.match(request);
        
        if (cachedResponse) {
            // Optionally update cache in background
            updateCacheInBackground(request, cache);
            return cachedResponse;
        }
        
        // Fetch from network and cache
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            cache.put(request, networkResponse.clone());
        }
        
        return networkResponse;
    } catch (error) {
        console.error('Cache first strategy failed:', error);
        return new Response('Offline content not available', { status: 503 });
    }
}

async function networkFirstWithCache(request) {
    try {
        // Try network first
        const networkResponse = await fetch(request);
        
        if (networkResponse.ok) {
            // Cache successful responses
            const cache = await caches.open(DATA_CACHE_NAME);
            cache.put(request, networkResponse.clone());
            return networkResponse;
        }
        
        throw new Error('Network response not ok');
    } catch (error) {
        // Fallback to cache
        const cache = await caches.open(DATA_CACHE_NAME);
        const cachedResponse = await cache.match(request);
        
        if (cachedResponse) {
            // Add offline indicator header
            const response = cachedResponse.clone();
            response.headers.set('X-Served-From', 'cache');
            return response;
        }
        
        // Return offline response
        return createOfflineResponse(request);
    }
}

async function networkFirstWithOfflinePage(request) {
    try {
        const networkResponse = await fetch(request);
        
        if (networkResponse.ok) {
            return networkResponse;
        }
        
        throw new Error('Network response not ok');
    } catch (error) {
        // Try to serve from cache
        const cache = await caches.open(STATIC_CACHE_NAME);
        const cachedResponse = await cache.match(request);
        
        if (cachedResponse) {
            return cachedResponse;
        }
        
        // Serve offline page
        return createOfflinePage();
    }
}

async function updateCacheInBackground(request, cache) {
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            cache.put(request, networkResponse.clone());
        }
    } catch (error) {
        console.log('Background cache update failed:', error);
    }
}

async function cacheInitialData() {
    try {
        const cache = await caches.open(DATA_CACHE_NAME);
        
        // Cache critical country data
        const countriesResponse = await fetch('./json/countries.json');
        if (countriesResponse.ok) {
            cache.put('./json/countries.json', countriesResponse.clone());
        }
        
        // Cache framework index
        const frameworksResponse = await fetch('./json/frameworks.json');
        if (frameworksResponse.ok) {
            cache.put('./json/frameworks.json', frameworksResponse.clone());
        }
        
        console.log('Service Worker: Initial data cached');
    } catch (error) {
        console.log('Service Worker: Failed to cache initial data', error);
    }
}

async function cacheCountryData(countryData) {
    try {
        const cache = await caches.open(DATA_CACHE_NAME);
        
        const response = new Response(JSON.stringify(countryData), {
            headers: {
                'Content-Type': 'application/json',
                'Cache-Control': 'max-age=3600'
            }
        });
        
        await cache.put(`/countries/${countryData.id}`, response);
        console.log(`Cached country data for ${countryData.id}`);
    } catch (error) {
        console.error('Failed to cache country data:', error);
    }
}

async function cacheSearchResults(searchData) {
    try {
        const cache = await caches.open(DATA_CACHE_NAME);
        const { query, results } = searchData;
        
        const response = new Response(JSON.stringify(results), {
            headers: {
                'Content-Type': 'application/json',
                'Cache-Control': 'max-age=1800' // 30 minutes
            }
        });
        
        await cache.put(`/search?q=${encodeURIComponent(query)}`, response);
        console.log(`Cached search results for: ${query}`);
    } catch (error) {
        console.error('Failed to cache search results:', error);
    }
}

async function clearAllCaches() {
    try {
        const cacheNames = await caches.keys();
        const deletePromises = cacheNames
            .filter(name => name.startsWith('openpiimap-'))
            .map(name => caches.delete(name));
        
        await Promise.all(deletePromises);
        console.log('All caches cleared');
        
        // Reinstall to rebuild caches
        self.registration.update();
    } catch (error) {
        console.error('Failed to clear caches:', error);
    }
}

async function getCacheStatus() {
    try {
        const cacheNames = await caches.keys();
        const status = {};
        
        for (const cacheName of cacheNames) {
            if (cacheName.startsWith('openpiimap-')) {
                const cache = await caches.open(cacheName);
                const keys = await cache.keys();
                status[cacheName] = {
                    size: keys.length,
                    items: keys.map(req => req.url)
                };
            }
        }
        
        return {
            caches: status,
            isOnline: navigator.onLine,
            lastSync: await getLastSyncTime()
        };
    } catch (error) {
        console.error('Failed to get cache status:', error);
        return { error: error.message };
    }
}

async function syncDataInBackground() {
    try {
        console.log('Service Worker: Starting background sync');
        
        // Fetch latest data
        const [countriesRes, frameworksRes] = await Promise.all([
            fetch('/json/countries.json'),
            fetch('/json/frameworks.json')
        ]);
        
        if (countriesRes.ok && frameworksRes.ok) {
            const cache = await caches.open(DATA_CACHE_NAME);
            
            await Promise.all([
                cache.put('/json/countries.json', countriesRes.clone()),
                cache.put('/json/frameworks.json', frameworksRes.clone())
            ]);
            
            // Store sync timestamp
            await setLastSyncTime(Date.now());
            
            // Notify clients of successful sync
            notifyClients({ type: 'SYNC_COMPLETE', success: true });
            
            console.log('Service Worker: Background sync complete');
        }
    } catch (error) {
        console.error('Service Worker: Background sync failed', error);
        notifyClients({ type: 'SYNC_COMPLETE', success: false, error: error.message });
    }
}

function createOfflineResponse(request) {
    const url = new URL(request.url);
    
    if (url.pathname.startsWith('/json/')) {
        // Return empty JSON response for API requests
        return new Response(JSON.stringify({
            error: 'Offline mode',
            message: 'This data is not available offline',
            cached: false
        }), {
            status: 503,
            headers: {
                'Content-Type': 'application/json',
                'X-Served-From': 'offline'
            }
        });
    }
    
    return new Response('Service unavailable while offline', {
        status: 503,
        headers: { 'Content-Type': 'text/plain' }
    });
}

function createOfflinePage() {
    const offlineHTML = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Offline - OpenPIIMap</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
            }
            .offline-container {
                max-width: 400px;
                padding: 2rem;
            }
            .offline-icon {
                font-size: 4rem;
                margin-bottom: 1rem;
            }
            h1 { margin-bottom: 0.5rem; }
            p { margin-bottom: 2rem; color: rgba(255, 255, 255, 0.8); }
            .btn {
                background: rgba(255, 255, 255, 0.2);
                border: 2px solid rgba(255, 255, 255, 0.3);
                padding: 0.75rem 1.5rem;
                border-radius: 0.5rem;
                color: white;
                text-decoration: none;
                display: inline-block;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="offline-container">
            <div class="offline-icon">📡</div>
            <h1>You're Offline</h1>
            <p>This page requires an internet connection. Please check your network and try again.</p>
            <a href="javascript:window.location.reload()" class="btn">Try Again</a>
        </div>
        
        <script>
            // Auto-reload when connection is restored
            window.addEventListener('online', () => {
                window.location.reload();
            });
        </script>
    </body>
    </html>
    `;
    
    return new Response(offlineHTML, {
        headers: { 'Content-Type': 'text/html' }
    });
}

async function getLastSyncTime() {
    try {
        const cache = await caches.open(DATA_CACHE_NAME);
        const response = await cache.match('/internal/last-sync');
        if (response) {
            const data = await response.json();
            return data.timestamp;
        }
    } catch (error) {
        console.log('No last sync time found');
    }
    return null;
}

async function setLastSyncTime(timestamp) {
    try {
        const cache = await caches.open(DATA_CACHE_NAME);
        const response = new Response(JSON.stringify({ timestamp }), {
            headers: { 'Content-Type': 'application/json' }
        });
        await cache.put('/internal/last-sync', response);
    } catch (error) {
        console.error('Failed to set last sync time:', error);
    }
}

function notifyClients(message) {
    self.clients.matchAll().then(clients => {
        clients.forEach(client => {
            client.postMessage(message);
        });
    });
}

// Push notification handler (for future use)
self.addEventListener('push', event => {
    if (event.data) {
        const data = event.data.json();
        const options = {
            body: data.body,
            icon: '/assets/icons/icon-192.png',
            badge: '/assets/icons/badge.png',
            vibrate: [100, 50, 100],
            data: data.data,
            actions: [
                {
                    action: 'view',
                    title: 'View Details',
                    icon: '/assets/icons/view.png'
                },
                {
                    action: 'dismiss',
                    title: 'Dismiss',
                    icon: '/assets/icons/dismiss.png'
                }
            ]
        };
        
        event.waitUntil(
            self.registration.showNotification(data.title, options)
        );
    }
});

// Notification click handler
self.addEventListener('notificationclick', event => {
    event.notification.close();
    
    if (event.action === 'view') {
        event.waitUntil(
            clients.openWindow(event.notification.data.url || '/')
        );
    }
});

console.log('Service Worker: Script loaded');
