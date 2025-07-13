// OpenPIIMap Static Site JavaScript

// Country data - will be populated from the existing structure
const countries = [
    { name: "Germany", framework: "GDPR", region: "Europe", file: "gdpr-germany.html", categories: 15 },
    { name: "France", framework: "GDPR", region: "Europe", file: "gdpr-france.html", categories: 15 },
    { name: "Ireland", framework: "GDPR", region: "Europe", file: "gdpr-ireland.html", categories: 15 },
    { name: "Netherlands", framework: "GDPR", region: "Europe", file: "gdpr-netherlands.html", categories: 15 },
    { name: "Spain", framework: "GDPR", region: "Europe", file: "gdpr-spain.html", categories: 15 },
    { name: "Italy", framework: "GDPR", region: "Europe", file: "gdpr-italy.html", categories: 15 },
    { name: "Poland", framework: "GDPR", region: "Europe", file: "gdpr-poland.html", categories: 15 },
    { name: "Belgium", framework: "GDPR", region: "Europe", file: "gdpr-belgium.html", categories: 15 },
    { name: "Austria", framework: "GDPR", region: "Europe", file: "gdpr-austria.html", categories: 15 },
    { name: "Sweden", framework: "GDPR", region: "Europe", file: "gdpr-sweden.html", categories: 15 },
    { name: "Finland", framework: "GDPR", region: "Europe", file: "gdpr-finland.html", categories: 15 },
    { name: "Denmark", framework: "GDPR", region: "Europe", file: "gdpr-denmark.html", categories: 15 },
    { name: "Norway", framework: "GDPR", region: "Europe", file: "gdpr-norway.html", categories: 15 },
    { name: "Iceland", framework: "GDPR", region: "Europe", file: "gdpr-iceland.html", categories: 15 },
    { name: "Greece", framework: "GDPR", region: "Europe", file: "gdpr-greece.html", categories: 15 },
    { name: "Liechtenstein", framework: "GDPR", region: "Europe", file: "gdpr-liechtenstein.html", categories: 15 },
    { name: "United Kingdom", framework: "UK GDPR", region: "Europe", file: "uk-gdpr-united-kingdom.html", categories: 15 },
    { name: "California, USA", framework: "CPRA", region: "North America", file: "cpra-california.html", categories: 12 },
    { name: "USA (Health)", framework: "HIPAA", region: "North America", file: "hippa-usa.html", categories: 18 },
    { name: "Canada", framework: "PIPEDA", region: "North America", file: "pipeda-canada.html", categories: 10 },
    { name: "Brazil", framework: "LGPD", region: "Latin America", file: "lgpd-brazil.html", categories: 14 },
    { name: "Mexico", framework: "LFPDPPP", region: "Latin America", file: "lfpdppp-mexico.html", categories: 11 },
    { name: "India", framework: "DPDPB", region: "Asia Pacific", file: "dpdpb-india.html", categories: 13 },
    { name: "Singapore", framework: "PDPA", region: "Asia Pacific", file: "pdpa-singapore.html", categories: 9 },
    { name: "South Korea", framework: "PIPA", region: "Asia Pacific", file: "pipa-south-korea.html", categories: 16 },
    { name: "Japan", framework: "APPI", region: "Asia Pacific", file: "appi-japan.html", categories: 8 },
    { name: "China", framework: "PIPL", region: "Asia Pacific", file: "pipl-china.html", categories: 12 },
    { name: "Indonesia", framework: "PDP Law", region: "Asia Pacific", file: "pdp-indonesia.html", categories: 10 },
    { name: "Australia", framework: "Privacy Act", region: "Asia Pacific", file: "privacyact-australia.html", categories: 7 },
    { name: "Nigeria", framework: "NDPR", region: "Other", file: "ndpr-nigeria.html", categories: 11 },
    { name: "UAE", framework: "UAE DPL", region: "Other", file: "uae-dpl-united-arab-emirates.html", categories: 9 },
    { name: "Switzerland", framework: "FADP", region: "Europe", file: "fadp-switzerland.html", categories: 10 }
];

// Framework color mapping
const frameworkColors = {
    'GDPR': 'framework-gdpr',
    'UK GDPR': 'framework-gdpr',
    'HIPAA': 'framework-hipaa',
    'CPRA': 'framework-cpra',
    'default': 'framework-default'
};

// Global state
let filteredCountries = [...countries];
let currentViewMode = 'card';

// DOM elements
let searchInput, frameworkFilter, regionFilter, countriesGrid, noResults;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeElements();
    setupEventListeners();
    renderCountries();
    updateStatistics();
});

function initializeElements() {
    searchInput = document.getElementById('countrySearch');
    frameworkFilter = document.getElementById('frameworkFilter');
    regionFilter = document.getElementById('regionFilter');
    countriesGrid = document.getElementById('countriesGrid');
    noResults = document.getElementById('noResults');
}

function setupEventListeners() {
    // Search functionality
    if (searchInput) {
        searchInput.addEventListener('input', debounce(handleSearch, 300));
    }
    
    // Framework filter buttons
    document.querySelectorAll('[data-framework]').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            // Remove active class from all buttons
            document.querySelectorAll('[data-framework]').forEach(btn => {
                btn.classList.remove('active');
            });
            // Add active class to clicked button
            this.classList.add('active');
            // Filter countries
            handleFrameworkFilter(this.dataset.framework);
        });
    });
    
    // Region filter if exists
    if (regionFilter) {
        regionFilter.addEventListener('change', handleFilter);
    }
    
    // View mode toggle if exists
    document.querySelectorAll('input[name="viewMode"]').forEach(radio => {
        radio.addEventListener('change', handleViewModeChange);
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function handleSearch() {
    const query = searchInput.value.toLowerCase().trim();
    applyFilters(query);
}

function handleFilter() {
    const query = searchInput.value.toLowerCase().trim();
    applyFilters(query);
}

function handleViewModeChange(e) {
    currentViewMode = e.target.id === 'cardView' ? 'card' : 'list';
    renderCountries();
}

function handleFrameworkFilter(framework) {
    if (framework === 'all') {
        filteredCountries = [...countries];
    } else {
        filteredCountries = countries.filter(country => 
            country.framework.toLowerCase().includes(framework.toLowerCase())
        );
    }
    
    // Apply search filter if there's a search term
    if (searchInput && searchInput.value.trim()) {
        const query = searchInput.value.toLowerCase().trim();
        filteredCountries = filteredCountries.filter(country =>
            country.name.toLowerCase().includes(query) ||
            country.framework.toLowerCase().includes(query) ||
            country.region.toLowerCase().includes(query)
        );
    }
    
    renderCountries();
}

function applyFilters(searchQuery = '') {
    const frameworkValue = frameworkFilter.value.toLowerCase();
    const regionValue = regionFilter.value.toLowerCase();
    
    filteredCountries = countries.filter(country => {
        const matchesSearch = !searchQuery || 
            country.name.toLowerCase().includes(searchQuery) ||
            country.framework.toLowerCase().includes(searchQuery) ||
            country.region.toLowerCase().includes(searchQuery);
        
        const matchesFramework = !frameworkValue || 
            country.framework.toLowerCase().includes(frameworkValue);
        
        const matchesRegion = !regionValue || 
            country.region.toLowerCase().replace(/\s+/g, '-') === regionValue;
        
        return matchesSearch && matchesFramework && matchesRegion;
    });
    
    renderCountries();
}

function renderCountries() {
    // Hide loading state if it exists
    const loadingState = document.getElementById('loadingState');
    if (loadingState) {
        loadingState.style.display = 'none';
    }
    
    if (!countriesGrid) {
        console.log('Countries grid not found on this page');
        return;
    }
    
    if (filteredCountries.length === 0) {
        countriesGrid.style.display = 'none';
        const noResultsState = document.getElementById('noResultsState');
        if (noResultsState) {
            noResultsState.classList.remove('d-none');
        }
        return;
    }
    
    countriesGrid.style.display = 'flex';
    const noResultsState = document.getElementById('noResultsState');
    if (noResultsState) {
        noResultsState.classList.add('d-none');
    }
    
    if (currentViewMode === 'card') {
        renderCardView();
    } else {
        renderListView();
    }
}

function renderCardView() {
    countriesGrid.className = 'row g-4';
    countriesGrid.innerHTML = filteredCountries.map(country => `
        <div class="col-lg-4 col-md-6">
            <div class="card country-card h-100">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title mb-0">${country.name}</h5>
                    <span class="framework-badge ${getFrameworkClass(country.framework)}">
                        ${country.framework}
                    </span>
                </div>
                <div class="card-body d-flex flex-column">
                    <div class="mb-3">
                        <small class="text-muted">
                            <i class="bi bi-geo-alt-fill me-1"></i>${country.region}
                        </small>
                    </div>
                    <div class="mb-3">
                        <small class="text-muted">
                            <i class="bi bi-list-check me-1"></i>${country.categories} PII Categories
                        </small>
                    </div>
                    <div class="mt-auto">
                        <a href="countries/${country.file}" class="btn btn-primary btn-sm w-100">
                            <i class="bi bi-eye me-1"></i>View Details
                        </a>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
}

function renderListView() {
    countriesGrid.className = 'row';
    countriesGrid.innerHTML = `
        <div class="col-12">
            <div class="table-responsive">
                <table class="table table-hover">
                    <thead class="table-light">
                        <tr>
                            <th>Country</th>
                            <th>Framework</th>
                            <th>Region</th>
                            <th>Categories</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${filteredCountries.map(country => `
                            <tr>
                                <td class="fw-semibold">${country.name}</td>
                                <td>
                                    <span class="framework-badge ${getFrameworkClass(country.framework)}">
                                        ${country.framework}
                                    </span>
                                </td>
                                <td class="text-muted">${country.region}</td>
                                <td class="text-muted">${country.categories}</td>
                                <td>
                                    <a href="countries/${country.file}" class="btn btn-outline-primary btn-sm">
                                        <i class="bi bi-eye me-1"></i>View
                                    </a>
                                </td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        </div>
    `;
}

function getFrameworkClass(framework) {
    return frameworkColors[framework] || frameworkColors.default;
}

function updateStatistics() {
    // Update stats based on current data
    const uniqueFrameworks = new Set(countries.map(c => c.framework)).size;
    const uniqueCountries = new Set(countries.map(c => c.name.split(',')[0])).size;
    
    // Update stat numbers if elements exist
    const statNumbers = document.querySelectorAll('.stat-number');
    if (statNumbers.length >= 4) {
        statNumbers[0].textContent = countries.length;
        statNumbers[1].textContent = uniqueFrameworks;
        statNumbers[2].textContent = `${uniqueCountries}+`;
        statNumbers[3].textContent = '100%';
    }
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add loading states
function showLoading(element) {
    element.classList.add('loading');
}

function hideLoading(element) {
    element.classList.remove('loading');
}

// Export for use in other scripts
window.OpenPIIMap = {
    countries,
    filteredCountries,
    renderCountries,
    applyFilters
};

// OpenPIIMap Main JavaScript
// Enhanced with offline capabilities and service worker support

// Global namespace
window.OpenPIIMap = window.OpenPIIMap || {};

// Configuration
const CONFIG = {
    apiUrl: './json/',
    cacheTimeout: 3600000, // 1 hour
    searchDebounce: 300,
    offlineEnabled: true
};

// Service Worker registration and offline capabilities
class OfflineManager {
    constructor() {
        this.isOnline = navigator.onLine;
        this.serviceWorker = null;
        this.cacheStatus = null;
        
        this.init();
    }
    
    async init() {
        // Register service worker
        if ('serviceWorker' in navigator && CONFIG.offlineEnabled) {
            try {
                this.serviceWorker = await navigator.serviceWorker.register('./sw.js');
                console.log('Service Worker registered successfully');
                
                // Listen for updates
                this.serviceWorker.addEventListener('updatefound', () => {
                    this.showUpdateNotification();
                });
                
                // Listen for messages from service worker
                navigator.serviceWorker.addEventListener('message', (event) => {
                    this.handleServiceWorkerMessage(event.data);
                });
                
                // Get initial cache status
                this.cacheStatus = await this.getCacheStatus();
                
            } catch (error) {
                console.error('Service Worker registration failed:', error);
            }
        }
        
        // Listen for online/offline events
        window.addEventListener('online', () => {
            this.isOnline = true;
            this.handleConnectivityChange();
        });
        
        window.addEventListener('offline', () => {
            this.isOnline = false;
            this.handleConnectivityChange();
        });
        
        // Show initial offline indicator if needed
        if (!this.isOnline) {
            this.showOfflineIndicator();
        }
    }
    
    async getCacheStatus() {
        if (!this.serviceWorker) return null;
        
        return new Promise((resolve) => {
            const messageChannel = new MessageChannel();
            messageChannel.port1.onmessage = (event) => {
                resolve(event.data);
            };
            
            this.serviceWorker.active?.postMessage(
                { type: 'GET_CACHE_STATUS' },
                [messageChannel.port2]
            );
        });
    }
    
    async syncData() {
        if (!this.serviceWorker || !this.isOnline) return;
        
        this.serviceWorker.active?.postMessage({ type: 'SYNC_DATA' });
        this.showToast('Syncing latest data...', 'info');
    }
    
    async clearCache() {
        if (!this.serviceWorker) return;
        
        this.serviceWorker.active?.postMessage({ type: 'CLEAR_CACHE' });
        this.showToast('Cache cleared successfully', 'success');
    }
    
    cacheCountryData(countryData) {
        if (!this.serviceWorker) return;
        
        this.serviceWorker.active?.postMessage({
            type: 'CACHE_COUNTRY_DATA',
            data: countryData
        });
    }
    
    cacheSearchResults(query, results) {
        if (!this.serviceWorker) return;
        
        this.serviceWorker.active?.postMessage({
            type: 'CACHE_SEARCH_RESULTS',
            data: { query, results }
        });
    }
    
    handleServiceWorkerMessage(message) {
        switch (message.type) {
            case 'SYNC_COMPLETE':
                if (message.success) {
                    this.showToast('Data synchronized successfully', 'success');
                } else {
                    this.showToast('Sync failed: ' + message.error, 'error');
                }
                break;
        }
    }
    
    handleConnectivityChange() {
        if (this.isOnline) {
            this.hideOfflineIndicator();
            this.syncData();
        } else {
            this.showOfflineIndicator();
        }
    }
    
    showOfflineIndicator() {
        let indicator = document.getElementById('offline-indicator');
        if (!indicator) {
            indicator = document.createElement('div');
            indicator.id = 'offline-indicator';
            indicator.className = 'offline-indicator';
            indicator.innerHTML = `
                <i class="bi bi-wifi-off me-2"></i>
                You're offline. Some features may be limited.
                <button class="btn btn-sm btn-outline-light ms-2" onclick="window.OpenPIIMap.offlineManager.syncData()">
                    Retry
                </button>
            `;
            document.body.appendChild(indicator);
        }
        indicator.style.display = 'flex';
    }
    
    hideOfflineIndicator() {
        const indicator = document.getElementById('offline-indicator');
        if (indicator) {
            indicator.style.display = 'none';
        }
    }
    
    showUpdateNotification() {
        this.showToast(
            'A new version is available. Refresh to update.',
            'info',
            {
                persistent: true,
                action: {
                    text: 'Refresh',
                    callback: () => window.location.reload()
                }
            }
        );
    }
    
    showToast(message, type = 'info', options = {}) {
        const iconClass = type === 'success' ? 'bi-check-circle-fill text-success' : 
                         type === 'error' ? 'bi-exclamation-triangle-fill text-danger' :
                         type === 'warning' ? 'bi-exclamation-triangle-fill text-warning' :
                         'bi-info-circle-fill text-info';
        
        const toast = document.createElement('div');
        toast.className = 'position-fixed top-0 end-0 p-3';
        toast.style.zIndex = '1100';
        
        const toastId = 'toast-' + Date.now();
        toast.innerHTML = `
            <div class="toast show" role="alert" id="${toastId}">
                <div class="toast-header">
                    <i class="${iconClass} me-2"></i>
                    <strong class="me-auto">OpenPIIMap</strong>
                    ${!options.persistent ? '<button type="button" class="btn-close" data-bs-dismiss="toast"></button>' : ''}
                </div>
                <div class="toast-body">
                    ${message}
                    ${options.action ? `
                        <div class="mt-2">
                            <button type="button" class="btn btn-primary btn-sm" onclick="${options.action.callback.toString()}(); document.getElementById('${toastId}').remove();">
                                ${options.action.text}
                            </button>
                        </div>
                    ` : ''}
                </div>
            </div>
        `;
        
        document.body.appendChild(toast);
        
        if (!options.persistent) {
            setTimeout(() => {
                if (document.body.contains(toast)) {
                    document.body.removeChild(toast);
                }
            }, 5000);
        }
    }
}

// Enhanced data manager with offline support
class DataManager {
    constructor() {
        this.cache = new Map();
        this.countries = [];
        this.frameworks = [];
        this.isLoading = false;
    }
    
    async loadData() {
        if (this.isLoading) return;
        this.isLoading = true;
        
        try {
            // For static site, we'll use the embedded data or try to load JSON files
            // First try to load from JSON files (if available)
            try {
                const [countriesRes, frameworksRes] = await Promise.all([
                    fetch('json/countries.json').then(r => r.json()),
                    fetch('json/frameworks.json').then(r => r.json()).catch(() => [])
                ]);
                
                this.countries = countriesRes || [];
                this.frameworks = frameworksRes || [];
                
                // Cache in localStorage for offline use
                this.saveToLocalStorage({
                    countries: this.countries,
                    frameworks: this.frameworks,
                    timestamp: Date.now()
                });
                
            } catch (jsonError) {
                console.log('JSON files not available, using fallback data');
                // Fallback to embedded data if JSON files aren't available
                this.loadFallbackData();
            }
            
            // Cache with service worker if available
            if (window.OpenPIIMap.offlineManager) {
                this.countries.forEach(country => {
                    window.OpenPIIMap.offlineManager.cacheCountryData(country);
                });
            }
            
        } catch (error) {
            console.error('Failed to load data:', error);
            
            // Fallback to localStorage or embedded data
            const cachedData = this.loadFromLocalStorage();
            if (cachedData) {
                this.countries = cachedData.countries || [];
                this.frameworks = cachedData.frameworks || [];
                
                window.OpenPIIMap.offlineManager?.showToast(
                    'Using cached data due to network error',
                    'warning'
                );
            } else {
                // Use embedded fallback data
                this.loadFallbackData();
                window.OpenPIIMap.offlineManager?.showToast(
                    'Using embedded data - JSON files not found',
                    'info'
                );
            }
        } finally {
            this.isLoading = false;
        }
    }
    
    loadFallbackData() {
        // Embedded fallback data for when JSON files aren't available
        this.countries = [
            {
                "id": "germany",
                "name": "Germany",
                "framework": "GDPR",
                "region": "Europe",
                "categories": 42,
                "lastUpdated": "2024-01-15T10:30:00Z"
            },
            {
                "id": "france",
                "name": "France",
                "framework": "GDPR", 
                "region": "Europe",
                "categories": 39,
                "lastUpdated": "2024-01-12T09:15:00Z"
            },
            {
                "id": "brazil",
                "name": "Brazil",
                "framework": "LGPD",
                "region": "Latin America",
                "categories": 35,
                "lastUpdated": "2024-01-06T12:30:00Z"
            },
            {
                "id": "california",
                "name": "California",
                "framework": "CPRA",
                "region": "North America",
                "categories": 33,
                "lastUpdated": "2024-01-14T11:45:00Z"
            },
            {
                "id": "canada",
                "name": "Canada",
                "framework": "PIPEDA",
                "region": "North America",
                "categories": 29,
                "lastUpdated": "2023-12-08T10:15:00Z"
            },
            {
                "id": "japan",
                "name": "Japan",
                "framework": "APPI",
                "region": "Asia Pacific",
                "categories": 24,
                "lastUpdated": "2023-11-18T16:45:00Z"
            },
            {
                "id": "singapore",
                "name": "Singapore",
                "framework": "PDPA",
                "region": "Asia Pacific",
                "categories": 27,
                "lastUpdated": "2023-12-03T09:20:00Z"
            },
            {
                "id": "united-kingdom",
                "name": "United Kingdom",
                "framework": "UK GDPR",
                "region": "Europe",
                "categories": 42,
                "lastUpdated": "2024-01-13T09:00:00Z"
            }
        ];
        
        this.frameworks = [
            {
                "id": "gdpr",
                "name": "General Data Protection Regulation",
                "abbreviation": "GDPR",
                "region": "Europe",
                "type": "comprehensive"
            },
            {
                "id": "lgpd",
                "name": "Lei Geral de Proteção de Dados",
                "abbreviation": "LGPD",
                "region": "Latin America",
                "type": "comprehensive"
            },
            {
                "id": "cpra",
                "name": "California Privacy Rights Act",
                "abbreviation": "CPRA",
                "region": "North America",
                "type": "comprehensive"
            }
        ];
    }
    
    saveToLocalStorage(data) {
        try {
            localStorage.setItem('openpiimap-data', JSON.stringify(data));
        } catch (error) {
            console.warn('Failed to cache data in localStorage:', error);
        }
    }
    
    loadFromLocalStorage() {
        try {
            const cached = localStorage.getItem('openpiimap-data');
            if (cached) {
                const data = JSON.parse(cached);
                // Check if cache is not too old (7 days)
                if (Date.now() - data.timestamp < 7 * 24 * 60 * 60 * 1000) {
                    return data;
                }
            }
        } catch (error) {
            console.warn('Failed to load cached data:', error);
        }
        return null;
    }
    
    searchCountries(query) {
        if (!query.trim()) return this.countries;
        
        const searchTerm = query.toLowerCase();
        const results = this.countries.filter(country => 
            country.name.toLowerCase().includes(searchTerm) ||
            country.framework.toLowerCase().includes(searchTerm) ||
            country.region.toLowerCase().includes(searchTerm)
        );
        
        // Cache search results
        if (window.OpenPIIMap.offlineManager) {
            window.OpenPIIMap.offlineManager.cacheSearchResults(query, results);
        }
        
        return results;
    }
    
    getCountryById(id) {
        return this.countries.find(country => country.id === id);
    }
    
    getFrameworks() {
        return [...new Set(this.countries.map(c => c.framework))];
    }
    
    getRegions() {
        return [...new Set(this.countries.map(c => c.region))];
    }
    
    filterCountries(filters) {
        return this.countries.filter(country => {
            if (filters.framework && country.framework !== filters.framework) return false;
            if (filters.region && country.region !== filters.region) return false;
            if (filters.search) {
                const searchTerm = filters.search.toLowerCase();
                return country.name.toLowerCase().includes(searchTerm) ||
                       country.framework.toLowerCase().includes(searchTerm) ||
                       country.region.toLowerCase().includes(searchTerm);
            }
            return true;
        });
    }
}

// Search functionality with debouncing
class SearchManager {
    constructor(dataManager) {
        this.dataManager = dataManager;
        this.searchTimeout = null;
        this.currentQuery = '';
        this.currentFilters = {};
    }
    
    init() {
        this.setupSearchInput();
        this.setupFilters();
    }
    
    setupSearchInput() {
        const searchInput = document.getElementById('countrySearch');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.debounceSearch(e.target.value);
            });
        }
    }
    
    setupFilters() {
        // Framework filter
        const frameworkFilter = document.getElementById('frameworkFilter');
        if (frameworkFilter) {
            frameworkFilter.addEventListener('change', (e) => {
                this.currentFilters.framework = e.target.value;
                this.performSearch();
            });
        }
        
        // Region filter
        const regionFilter = document.getElementById('regionFilter');
        if (regionFilter) {
            regionFilter.addEventListener('change', (e) => {
                this.currentFilters.region = e.target.value;
                this.performSearch();
            });
        }
        
        // View mode toggles
        document.querySelectorAll('[data-view-mode]').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const mode = e.target.closest('[data-view-mode]').dataset.viewMode;
                this.setViewMode(mode);
            });
        });
    }
    
    debounceSearch(query) {
        clearTimeout(this.searchTimeout);
        this.currentQuery = query;
        
        this.searchTimeout = setTimeout(() => {
            this.performSearch();
        }, CONFIG.searchDebounce);
    }
    
    performSearch() {
        const filters = {
            ...this.currentFilters,
            search: this.currentQuery
        };
        
        const results = this.dataManager.filterCountries(filters);
        this.displayResults(results);
        this.updateResultsCount(results.length);
    }
    
    displayResults(countries) {
        const container = document.getElementById('countriesContainer');
        if (!container) return;
        
        // Show loading state
        container.innerHTML = '<div class="text-center py-4"><div class="spinner-border" role="status"></div></div>';
        
        // Simulate brief loading for better UX
        setTimeout(() => {
            if (countries.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-5">
                        <i class="bi bi-search display-4 text-muted mb-3"></i>
                        <h5>No countries found</h5>
                        <p class="text-muted">Try adjusting your search criteria</p>
                    </div>
                `;
                return;
            }
            
            const currentViewMode = this.getCurrentViewMode();
            
            if (currentViewMode === 'list') {
                this.displayAsList(countries, container);
            } else {
                this.displayAsCards(countries, container);
            }
        }, 100);
    }
    
    displayAsCards(countries, container) {
        container.innerHTML = countries.map(country => `
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="card country-card h-100">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-3">
                            <h5 class="card-title mb-0">${country.name}</h5>
                            <span class="framework-badge ${this.getFrameworkClass(country.framework)}">
                                ${country.framework}
                            </span>
                        </div>
                        
                        <div class="country-meta">
                            <div class="meta-item">
                                <i class="bi bi-geo-alt-fill"></i>
                                <span>${country.region}</span>
                            </div>
                            <div class="meta-item">
                                <i class="bi bi-list-ul"></i>
                                <span>${country.categories || 0} categories</span>
                            </div>
                            <div class="meta-item">
                                <i class="bi bi-calendar-event"></i>
                                <span>Updated ${this.formatDate(country.lastUpdated)}</span>
                            </div>
                        </div>
                        
                        <div class="mt-3">
                            <a href="countries/${country.framework.toLowerCase()}-${country.id}.html" 
                               class="btn btn-primary btn-sm">
                                <i class="bi bi-arrow-right me-1"></i>View Details
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }
    
    displayAsList(countries, container) {
        container.innerHTML = `
            <div class="col-12">
                <div class="table-responsive">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>Country</th>
                                <th>Framework</th>
                                <th>Region</th>
                                <th>Categories</th>
                                <th>Last Updated</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${countries.map(country => `
                                <tr>
                                    <td>
                                        <strong>${country.name}</strong>
                                    </td>
                                    <td>
                                        <span class="framework-badge ${this.getFrameworkClass(country.framework)}">
                                            ${country.framework}
                                        </span>
                                    </td>
                                    <td>${country.region}</td>
                                    <td>${country.categories || 0}</td>
                                    <td>${this.formatDate(country.lastUpdated)}</td>
                                    <td>
                                        <a href="countries/${country.framework.toLowerCase()}-${country.id}.html" 
                                           class="btn btn-primary btn-sm">
                                            View Details
                                        </a>
                                    </td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
    }
    
    getCurrentViewMode() {
        const activeBtn = document.querySelector('[data-view-mode].active');
        return activeBtn ? activeBtn.dataset.viewMode : 'cards';
    }
    
    setViewMode(mode) {
        // Update button states
        document.querySelectorAll('[data-view-mode]').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-view-mode="${mode}"]`)?.classList.add('active');
        
        // Re-render with new view mode
        this.performSearch();
    }
    
    updateResultsCount(count) {
        const counters = document.querySelectorAll('.results-count');
        counters.forEach(counter => {
            counter.textContent = count;
        });
    }
    
    getFrameworkClass(framework) {
        const classes = {
            'GDPR': 'gdpr',
            'LGPD': 'lgpd',
            'CCPA': 'ccpa',
            'CPRA': 'cpra',
            'HIPAA': 'hipaa',
            'PIPEDA': 'pipeda'
        };
        return classes[framework] || 'other';
    }
    
    formatDate(dateString) {
        if (!dateString) return 'Unknown';
        try {
            return new Date(dateString).toLocaleDateString();
        } catch {
            return dateString;
        }
    }
}

// App initialization
class OpenPIIMapApp {
    constructor() {
        this.offlineManager = new OfflineManager();
        this.dataManager = new DataManager();
        this.searchManager = new SearchManager(this.dataManager);
        
        // Export to global namespace
        window.OpenPIIMap.offlineManager = this.offlineManager;
        window.OpenPIIMap.dataManager = this.dataManager;
        window.OpenPIIMap.searchManager = this.searchManager;
    }
    
    async init() {
        try {
            // Load data
            await this.dataManager.loadData();
            
            // Initialize search
            this.searchManager.init();
            
            // Initialize any page-specific functionality
            this.initializePageFeatures();
            
            // Initial search to show all countries
            this.searchManager.performSearch();
            
            console.log('OpenPIIMap initialized successfully');
            
        } catch (error) {
            console.error('Failed to initialize OpenPIIMap:', error);
            this.offlineManager.showToast('Failed to initialize application', 'error');
        }
    }
    
    initializePageFeatures() {
        // Initialize based on current page
        const path = window.location.pathname;
        
        if (path.includes('dashboard.html')) {
            this.initializeDashboard();
        } else if (path.includes('map.html')) {
            this.initializeMap();
        } else if (path.includes('compare.html')) {
            this.initializeComparison();
        }
    }
    
    initializeDashboard() {
        // Dashboard-specific initialization
        window.OpenPIIMap.countries = this.dataManager.countries;
    }
    
    initializeMap() {
        // Map-specific initialization
        if (typeof window.initializeMap === 'function') {
            window.initializeMap(this.dataManager.countries);
        }
    }
    
    initializeComparison() {
        // Comparison tool initialization
        if (typeof window.initializeComparison === 'function') {
            window.initializeComparison(this.dataManager.countries);
        }
    }
}

// CSS for offline indicator
const offlineCSS = `
.offline-indicator {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    color: white;
    padding: 0.75rem 1rem;
    text-align: center;
    z-index: 1000;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 500;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.offline-indicator button {
    border: 1px solid rgba(255,255,255,0.3) !important;
    color: white !important;
}

.offline-indicator button:hover {
    background: rgba(255,255,255,0.1) !important;
    border-color: rgba(255,255,255,0.5) !important;
}

/* Adjust body padding when offline indicator is shown */
body.offline-mode {
    padding-top: 60px;
}
`;

// Inject CSS
const style = document.createElement('style');
style.textContent = offlineCSS;
document.head.appendChild(style);

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const app = new OpenPIIMapApp();
    app.init();
});

// Export for global access
window.OpenPIIMap.app = OpenPIIMapApp;
