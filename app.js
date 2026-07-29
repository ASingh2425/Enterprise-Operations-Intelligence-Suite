// Enterprise Operations Intelligence Suite — Dynamic Slicer & Chart Engine

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initModal();
    initSlicers();
    renderDashboard('ALL', '2025');
});

// Page Metadata
const pageTitles = {
    'page-1': { title: 'Executive Dashboard', subtitle: 'Real-time Global Operations Monitoring & Enterprise KPIs' },
    'page-2': { title: 'Sales Analytics', subtitle: 'Revenue, Profit Heatmaps, Category Trends & Dynamic Drilldown' },
    'page-3': { title: 'Supply Chain Analytics', subtitle: 'Fulfillment Capacity Utilization, Lead Times & Supplier Ratings' },
    'page-4': { title: 'Logistics Dashboard', subtitle: 'Carrier SLA On-Time Delivery, Route Costs & Delay Heatmaps' },
    'page-5': { title: 'Demand Forecasting', subtitle: '30/60/90/180-Day Time Series Predictions & 95% Confidence Intervals' },
    'page-6': { title: 'Customer Intelligence', subtitle: 'RFM Customer Segmentation, Lifetime Value (LTV) & Retention' },
    'page-7': { title: 'Profitability Analysis', subtitle: 'Gross Sales to Net Profit Waterfall Breakdown & Margins' },
    'page-8': { title: 'Inventory Optimization', subtitle: 'ABC Pareto Classification, EOQ Reorder Point & Days of Inventory' },
    'page-9': { title: 'Risk Monitoring', subtitle: 'Supplier Risk Scores, Stockout Probabilities & Anomaly Detection' },
    'page-10': { title: 'Executive AI Insights', subtitle: 'Automated Natural Language Recommendations & Strategic Action Items' }
};

// Global Store for Chart.js instances
const chartInstances = {};

// Palette
const colors = {
    cyan: '#38bdf8',
    indigo: '#818cf8',
    emerald: '#34d399',
    rose: '#f87171',
    amber: '#fbbf24',
    purple: '#a78bfa',
    muted: '#94a3b8',
    gridBorder: 'rgba(255, 255, 255, 0.08)'
};

// Regional & Period Multiplier Data Model
const regionalData = {
    'ALL': {
        revenue: 142.8, profit: 46.4, margin: 32.5, orders: 520000, perfectOrder: 94.8, returnRate: 4.80, onTime: 96.2,
        catRevenue: [54.8, 38.2, 29.5, 20.3],
        whUnits: [580, 490, 420, 380, 310, 260],
        carrierSLA: [96.4, 95.2, 94.1, 92.5, 86.2],
        rfm: [3200, 4800, 2900, 2500, 1600],
        waterfall: [160.0, -17.2, 142.8, -85.2, -11.2, 46.4],
        abc: [114.2, 21.4, 7.2],
        doi: [48, 52, 38, 44, 32],
        anomalies: [142, 88, 54, 31],
        stockout: [0.18, 0.42, 0.12, 0.28, 0.08]
    },
    'North America': {
        revenue: 64.2, profit: 21.2, margin: 33.0, orders: 234000, perfectOrder: 95.4, returnRate: 4.30, onTime: 97.1,
        catRevenue: [25.4, 17.2, 12.8, 8.8],
        whUnits: [580, 420, 310, 220, 180, 140],
        carrierSLA: [97.2, 95.8, 94.9, 93.1, 88.0],
        rfm: [1500, 2200, 1200, 950, 600],
        waterfall: [72.0, -7.8, 64.2, -37.8, -5.2, 21.2],
        abc: [51.4, 9.6, 3.2],
        doi: [44, 38, 32, 36, 28],
        anomalies: [52, 31, 18, 12],
        stockout: [0.12, 0.28, 0.08, 0.15, 0.05]
    },
    'Europe': {
        revenue: 48.6, profit: 15.5, margin: 31.9, orders: 176000, perfectOrder: 94.1, returnRate: 5.10, onTime: 95.3,
        catRevenue: [18.2, 13.4, 10.2, 6.8],
        whUnits: [490, 380, 260, 190, 150, 110],
        carrierSLA: [95.8, 94.9, 93.5, 91.8, 85.1],
        rfm: [1100, 1600, 1000, 900, 600],
        waterfall: [55.0, -6.4, 48.6, -29.2, -3.9, 15.5],
        abc: [38.8, 7.3, 2.5],
        doi: [52, 44, 40, 38, 34],
        anomalies: [58, 36, 22, 11],
        stockout: [0.24, 0.42, 0.18, 0.31, 0.10]
    },
    'APAC': {
        revenue: 30.0, profit: 9.7, margin: 32.3, orders: 110000, perfectOrder: 93.8, returnRate: 5.20, onTime: 94.8,
        catRevenue: [11.2, 7.6, 6.5, 4.7],
        whUnits: [380, 260, 180, 140, 110, 90],
        carrierSLA: [95.1, 94.2, 92.8, 90.5, 84.0],
        rfm: [600, 1000, 700, 650, 400],
        waterfall: [33.0, -3.0, 30.0, -18.2, -2.1, 9.7],
        abc: [24.0, 4.5, 1.5],
        doi: [44, 48, 36, 40, 30],
        anomalies: [32, 21, 14, 8],
        stockout: [0.18, 0.35, 0.10, 0.22, 0.06]
    }
};

const periodMultipliers = {
    '2025': 1.0,
    '2024': 0.88,
    '2023': 0.76
};

function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const pages = document.querySelectorAll('.page-content');
    const titleEl = document.getElementById('current-page-title');
    const subtitleEl = document.getElementById('current-page-subtitle');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const pageId = item.getAttribute('data-page');

            navItems.forEach(n => n.classList.remove('active'));
            pages.forEach(p => p.classList.remove('active'));

            item.classList.add('active');
            const targetPage = document.getElementById(pageId);
            if (targetPage) targetPage.classList.add('active');

            if (pageTitles[pageId]) {
                titleEl.textContent = pageTitles[pageId].title;
                subtitleEl.textContent = pageTitles[pageId].subtitle;
            }
        });
    });
}

function initModal() {
    const modal = document.getElementById('dax-modal');
    const btnOpen = document.getElementById('btn-dax-modal');
    const btnClose = document.getElementById('btn-close-dax');

    if (btnOpen) btnOpen.addEventListener('click', () => modal.classList.add('active'));
    if (btnClose) btnClose.addEventListener('click', () => modal.classList.remove('active'));
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('active');
        });
    }
}

function initSlicers() {
    const regionSlicer = document.getElementById('slicer-region');
    const periodSlicer = document.getElementById('slicer-period');
    const btnReset = document.getElementById('btn-reset-filters');

    if (regionSlicer) {
        regionSlicer.addEventListener('change', () => {
            renderDashboard(regionSlicer.value, periodSlicer.value);
        });
    }

    if (periodSlicer) {
        periodSlicer.addEventListener('change', () => {
            renderDashboard(regionSlicer.value, periodSlicer.value);
        });
    }

    if (btnReset) {
        btnReset.addEventListener('click', () => {
            regionSlicer.value = 'ALL';
            periodSlicer.value = '2025';
            renderDashboard('ALL', '2025');
        });
    }
}

function renderDashboard(region, period) {
    const base = regionalData[region] || regionalData['ALL'];
    const mult = periodMultipliers[period] || 1.0;

    // 1. Update KPI Cards dynamically
    const revVal = (base.revenue * mult).toFixed(1);
    const profVal = (base.profit * mult).toFixed(1);
    const ordersVal = Math.round(base.orders * mult).toLocaleString();

    document.querySelector('#page-1 .kpi-card:nth-child(1) .kpi-value').textContent = `$${revVal}M`;
    document.querySelector('#page-1 .kpi-card:nth-child(2) .kpi-value').textContent = `$${profVal}M`;
    document.querySelector('#page-1 .kpi-card:nth-child(3) .kpi-value').textContent = ordersVal;
    document.querySelector('#page-1 .kpi-card:nth-child(4) .kpi-value').textContent = `${base.perfectOrder}%`;
    document.querySelector('#page-1 .kpi-card:nth-child(5) .kpi-value').textContent = `${base.returnRate}%`;
    document.querySelector('#page-1 .kpi-card:nth-child(6) .kpi-value').textContent = `${base.onTime}%`;

    // 2. Render / Update Charts dynamically
    updateCharts(base, mult, region);

    // 3. Render Executive AI Insights dynamically
    loadExecutiveInsights(region);
}

function updateCharts(base, mult, region) {
    // 1. Executive Line Trend
    const monthlyRev = [10.5, 11.2, 12.1, 11.8, 12.9, 13.5, 14.1, 13.8, 14.9, 15.6, 16.8, 18.2].map(v => +(v * (base.revenue / 142.8) * mult).toFixed(1));
    const monthlyProf = [3.2, 3.5, 3.9, 3.7, 4.1, 4.3, 4.6, 4.5, 4.8, 5.1, 5.5, 6.1].map(v => +(v * (base.profit / 46.4) * mult).toFixed(1));

    createOrUpdateChart('chart-exec-trend', 'line', {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
            { label: 'Revenue ($M)', data: monthlyRev, borderColor: colors.cyan, backgroundColor: 'rgba(56, 189, 248, 0.1)', fill: true, tension: 0.3 },
            { label: 'Profit ($M)', data: monthlyProf, borderColor: colors.emerald, backgroundColor: 'transparent', borderDash: [5, 5], tension: 0.3 }
        ]
    });

    // Executive Region Donut
    const regionDonutData = region === 'ALL' ? [64.2 * mult, 48.6 * mult, 30.0 * mult] : (region === 'North America' ? [64.2 * mult, 0, 0] : (region === 'Europe' ? [0, 48.6 * mult, 0] : [0, 0, 30.0 * mult]));
    createOrUpdateChart('chart-exec-region', 'doughnut', {
        labels: ['North America', 'Europe', 'APAC'],
        datasets: [{ data: regionDonutData, backgroundColor: [colors.cyan, colors.indigo, colors.emerald] }]
    }, { cutout: '70%' });

    // 2. Sales Categories
    const scaledCat = base.catRevenue.map(v => +(v * mult).toFixed(1));
    createOrUpdateChart('chart-sales-cat', 'bar', {
        labels: ['Technology', 'Furniture', 'Office Supplies', 'Logistics Gear'],
        datasets: [{ label: 'Net Revenue ($M)', data: scaledCat, backgroundColor: [colors.cyan, colors.indigo, colors.purple, colors.emerald] }]
    });

    // Top SKUs
    createOrUpdateChart('chart-sales-top-skus', 'bar', {
        labels: ['PROD-0001 (Laptop)', 'PROD-0005 (Desk)', 'PROD-0012 (Phone)', 'PROD-0020 (Chair)', 'PROD-0033 (Scanner)'],
        datasets: [{ label: 'Gross Margin %', data: [52.4, 48.1, 45.3, 42.8, 41.5], backgroundColor: colors.emerald }]
    }, { indexAxis: 'y' });

    // 3. Supply Chain Warehouse Capacity
    const scaledWh = base.whUnits.map(v => Math.round(v * mult));
    createOrUpdateChart('chart-wh-capacity', 'bar', {
        labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON', 'WH-APAC-SYD'],
        datasets: [
            { label: 'Units Held (k)', data: scaledWh, backgroundColor: colors.cyan },
            { label: 'Max Capacity (k)', data: [750, 600, 500, 450, 400, 350], backgroundColor: 'rgba(255,255,255,0.1)' }
        ]
    });

    // Supplier Risk Radar
    createOrUpdateChart('chart-supplier-risk', 'radar', {
        labels: ['Rating (5.0)', 'On-Time %', 'Quality / Defect Rate', 'Lead Time Days', 'Risk Index'],
        datasets: [
            { label: 'Top Preferred Vendor', data: [4.9, 98, 99, 4, 12], borderColor: colors.emerald, backgroundColor: 'rgba(52, 211, 153, 0.2)' },
            { label: 'At-Risk Vendor (SUP-014)', data: [3.3, 82, 94, 18, 58], borderColor: colors.rose, backgroundColor: 'rgba(248, 113, 113, 0.2)' }
        ]
    });

    // 4. Carrier SLA
    createOrUpdateChart('chart-carrier-sla', 'bar', {
        labels: ['Amazon Air', 'DHL Express', 'FedEx', 'UPS', 'Regional Freight'],
        datasets: [{ label: 'On-Time SLA %', data: base.carrierSLA, backgroundColor: [colors.emerald, colors.cyan, colors.indigo, colors.amber, colors.rose] }]
    }, { indexAxis: 'y' });

    // Shipping Cost Line
    createOrUpdateChart('chart-shipping-cost', 'line', {
        labels: ['Route US-EU', 'Route US-APAC', 'Route EU-APAC', 'Domestic US', 'Domestic EU'],
        datasets: [{ label: 'Avg Shipping Cost ($)', data: [28.5, 34.2, 31.8, 12.4, 14.1], borderColor: colors.amber, backgroundColor: 'rgba(251, 191, 36, 0.1)', fill: true }]
    });

    // 5. Demand Forecast
    const forecastDates = Array.from({length: 30}, (_, i) => `Day ${i+1}`);
    const baseDemand = 1780 * mult;
    const actualData = [1420, 1450, 1480, 1410, 1510, 1530, 1580, 1600, 1590, 1650, 1680, 1720, 1710, 1750, 1780].map(v => Math.round(v * mult));
    const predicted = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, Math.round(baseDemand), Math.round(baseDemand*1.02), Math.round(baseDemand*1.04), Math.round(baseDemand*1.05), Math.round(baseDemand*1.07)];
    const upperBound = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, Math.round(baseDemand), Math.round(baseDemand*1.08), Math.round(baseDemand*1.10), Math.round(baseDemand*1.12), Math.round(baseDemand*1.15)];
    const lowerBound = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, Math.round(baseDemand), Math.round(baseDemand*0.96), Math.round(baseDemand*0.97), Math.round(baseDemand*0.98), Math.round(baseDemand*0.99)];

    createOrUpdateChart('chart-demand-forecast', 'line', {
        labels: forecastDates.slice(0, 19),
        datasets: [
            { label: 'Historical Orders', data: actualData, borderColor: colors.cyan, tension: 0.2 },
            { label: 'Holt-Winters Forecast', data: predicted, borderColor: colors.indigo, borderDash: [6, 6], tension: 0.2 },
            { label: '95% Upper Bound', data: upperBound, borderColor: 'rgba(52, 211, 153, 0.5)', borderDash: [2, 2], fill: '+1', backgroundColor: 'rgba(52, 211, 153, 0.08)' },
            { label: '95% Lower Bound', data: lowerBound, borderColor: 'rgba(52, 211, 153, 0.5)', borderDash: [2, 2], fill: false }
        ]
    });

    // 6. Customer RFM
    const scaledRfm = base.rfm.map(v => Math.round(v * mult));
    createOrUpdateChart('chart-rfm-segments', 'pie', {
        labels: ['Champions', 'Loyal Customers', 'Promising', 'At Risk', 'Lost / Churned'],
        datasets: [{ data: scaledRfm, backgroundColor: [colors.emerald, colors.cyan, colors.indigo, colors.amber, colors.rose] }]
    });

    createOrUpdateChart('chart-customer-ltv', 'bar', {
        labels: ['Champions', 'Loyal Customers', 'Promising', 'At Risk', 'Lost'],
        datasets: [{ label: 'Avg Lifetime Value ($)', data: [4250, 2850, 1450, 920, 380], backgroundColor: colors.cyan }]
    });

    // 7. Waterfall Profit
    const scaledWaterfall = base.waterfall.map(v => +(v * mult).toFixed(1));
    createOrUpdateChart('chart-waterfall-profit', 'bar', {
        labels: ['Gross Sales', 'Discounts', 'Net Revenue', 'COGS', 'Shipping Cost', 'Net Profit'],
        datasets: [{ label: 'Financial Flow ($M)', data: scaledWaterfall, backgroundColor: [colors.cyan, colors.rose, colors.indigo, colors.rose, colors.amber, colors.emerald] }]
    });

    // 8. ABC Pareto
    const scaledAbc = base.abc.map(v => +(v * mult).toFixed(1));
    createOrUpdateChart('chart-abc-pareto', 'bar', {
        labels: ['Class A (Top SKUs)', 'Class B (Mid SKUs)', 'Class C (Tail SKUs)'],
        datasets: [{ label: 'Revenue Share ($M)', data: scaledAbc, backgroundColor: [colors.cyan, colors.indigo, colors.muted] }]
    });

    createOrUpdateChart('chart-inventory-doi', 'bar', {
        labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON'],
        datasets: [{ label: 'Days of Inventory (DOI)', data: base.doi, backgroundColor: colors.purple }]
    });

    // 9. Risk Anomalies & Stockout
    createOrUpdateChart('chart-anomalies', 'bar', {
        labels: ['Freight Cost Spikes', 'Margin Compression', 'Defect Outliers', 'Return Surges'],
        datasets: [{ label: 'Detected Anomalies', data: base.anomalies, backgroundColor: colors.rose }]
    });

    createOrUpdateChart('chart-stockout-risk', 'bar', {
        labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON'],
        datasets: [{ label: 'Stockout Risk Index', data: base.stockout, backgroundColor: colors.amber }]
    });
}

function createOrUpdateChart(canvasId, type, data, extraOptions = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    if (chartInstances[canvasId]) {
        chartInstances[canvasId].destroy();
    }

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { labels: { color: colors.muted, font: { family: 'Inter', size: 11 } } }
        },
        scales: (type === 'pie' || type === 'doughnut' || type === 'radar') ? {} : {
            x: { ticks: { color: colors.muted }, grid: { color: colors.gridBorder } },
            y: { ticks: { color: colors.muted }, grid: { color: colors.gridBorder } }
        },
        ...extraOptions
    };

    chartInstances[canvasId] = new Chart(canvas, { type, data, options });
}

function loadExecutiveInsights(region) {
    const container = document.getElementById('insights-cards-list');
    if (!container) return;

    const allInsights = [
        {
            InsightID: 'INS-01',
            Priority: 'CRITICAL',
            Title: 'Inventory Reduction Opportunity at WH-US-WEST-1',
            Recommendation: 'Current stock level at WH-US-WEST-1 stands at 580,000 units. Reduce holding inventory by 18% to free up ~$420,000 in working capital and lower holding costs.',
            Category: 'Inventory Optimization',
            Region: 'North America'
        },
        {
            InsightID: 'INS-02',
            Priority: 'CRITICAL',
            Title: 'Vendor Quality Audit Recommended for Global Supplier 14',
            Recommendation: 'Supplier 14 exhibits a defect rate of 4.25% (Threshold: 1.5%) and average delivery delay of 18 days. Contract renegotiation or vendor replacement recommended.',
            Category: 'Supplier Risk',
            Region: 'Europe'
        },
        {
            InsightID: 'INS-03',
            Priority: 'HIGH',
            Title: 'Carrier SLA Late Delivery Alert',
            Recommendation: 'Regional Freight Co accounts for 42% of all late shipments. Shift 15% volume to Amazon Air Logistics to boost overall SLA to 97.1%.',
            Category: 'Logistics SLA',
            Region: 'North America'
        },
        {
            InsightID: 'INS-04',
            Priority: 'HIGH',
            Title: 'Margin Compression in European Fulfillment Hub',
            Recommendation: 'Net profit margin at WH-EU-CENT-1 is lagging target by 4.2%. Re-evaluate localized freight costs and order fulfillment routes.',
            Category: 'Profitability',
            Region: 'Europe'
        },
        {
            InsightID: 'INS-05',
            Priority: 'MEDIUM',
            Title: 'APAC Demand Surge in Technology Category',
            Recommendation: 'Technology products in APAC generated $11.2M in net revenue. Maintain 30-day safety stock buffer to capture projected peak demand.',
            Category: 'Sales & Demand',
            Region: 'APAC'
        }
    ];

    const filtered = (region === 'ALL') ? allInsights : allInsights.filter(i => i.Region === region || i.Region === 'ALL');

    container.innerHTML = filtered.map(item => `
        <div class="insight-item">
            <div class="insight-top">
                <span class="insight-tag ${item.Priority}">${item.Priority}</span>
                <span style="font-size: 0.75rem; color: var(--text-muted);">${item.Category} (${item.Region})</span>
            </div>
            <div class="insight-title">${item.Title}</div>
            <div class="insight-body">${item.Recommendation}</div>
        </div>
    `).join('');
}
