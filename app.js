// Enterprise Operations Intelligence Suite JS Engine

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initModal();
    initCharts();
    loadExecutiveInsights();
});

// Page Title Metadata
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

    document.getElementById('btn-reset-filters').addEventListener('click', () => {
        document.getElementById('slicer-region').value = 'ALL';
        document.getElementById('slicer-period').value = '2025';
        alert('Filters successfully reset to default global view!');
    });
}

function initModal() {
    const modal = document.getElementById('dax-modal');
    const btnOpen = document.getElementById('btn-dax-modal');
    const btnClose = document.getElementById('btn-close-dax');

    btnOpen.addEventListener('click', () => modal.classList.add('active'));
    btnClose.addEventListener('click', () => modal.classList.remove('active'));
    modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('active');
    });
}

// Chart.js Color Palette
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

function initCharts() {
    // 1. Executive Monthly Trend
    new Chart(document.getElementById('chart-exec-trend'), {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [
                {
                    label: 'Revenue ($M)',
                    data: [10.5, 11.2, 12.1, 11.8, 12.9, 13.5, 14.1, 13.8, 14.9, 15.6, 16.8, 18.2],
                    borderColor: colors.cyan,
                    backgroundColor: 'rgba(56, 189, 248, 0.1)',
                    fill: true,
                    tension: 0.3
                },
                {
                    label: 'Profit ($M)',
                    data: [3.2, 3.5, 3.9, 3.7, 4.1, 4.3, 4.6, 4.5, 4.8, 5.1, 5.5, 6.1],
                    borderColor: colors.emerald,
                    backgroundColor: 'transparent',
                    borderDash: [5, 5],
                    tension: 0.3
                }
            ]
        },
        options: getChartDefaults()
    });

    // Executive Region Donut
    new Chart(document.getElementById('chart-exec-region'), {
        type: 'doughnut',
        data: {
            labels: ['North America', 'Europe', 'APAC'],
            datasets: [{
                data: [64.2, 48.6, 30.0],
                backgroundColor: [colors.cyan, colors.indigo, colors.emerald]
            }]
        },
        options: { ...getChartDefaults(), cutout: '70%' }
    });

    // 2. Sales Category
    new Chart(document.getElementById('chart-sales-cat'), {
        type: 'bar',
        data: {
            labels: ['Technology', 'Furniture', 'Office Supplies', 'Logistics Gear'],
            datasets: [{
                label: 'Net Revenue ($M)',
                data: [54.8, 38.2, 29.5, 20.3],
                backgroundColor: [colors.cyan, colors.indigo, colors.purple, colors.emerald]
            }]
        },
        options: getChartDefaults()
    });

    // Top SKUs
    new Chart(document.getElementById('chart-sales-top-skus'), {
        type: 'bar',
        data: {
            labels: ['PROD-0001 (Laptop)', 'PROD-0005 (Desk)', 'PROD-0012 (Phone)', 'PROD-0020 (Chair)', 'PROD-0033 (Scanner)'],
            datasets: [{
                label: 'Gross Margin %',
                data: [52.4, 48.1, 45.3, 42.8, 41.5],
                backgroundColor: colors.emerald
            }]
        },
        options: { ...getChartDefaults(), indexAxis: 'y' }
    });

    // 3. Supply Chain Warehouse Capacity
    new Chart(document.getElementById('chart-wh-capacity'), {
        type: 'bar',
        data: {
            labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON', 'WH-APAC-SYD'],
            datasets: [
                { label: 'Current Units Held (k)', data: [580, 490, 420, 380, 310, 260], backgroundColor: colors.cyan },
                { label: 'Max Capacity (k)', data: [750, 600, 500, 450, 400, 350], backgroundColor: 'rgba(255,255,255,0.1)' }
            ]
        },
        options: getChartDefaults()
    });

    // Supplier Risk
    new Chart(document.getElementById('chart-supplier-risk'), {
        type: 'radar',
        data: {
            labels: ['Rating (5.0)', 'On-Time %', 'Quality / Defect Rate', 'Lead Time Days', 'Risk Index'],
            datasets: [
                { label: 'Top Preferred Vendor', data: [4.9, 98, 99, 4, 12], borderColor: colors.emerald, backgroundColor: 'rgba(52, 211, 153, 0.2)' },
                { label: 'At-Risk Vendor (SUP-014)', data: [3.3, 82, 94, 18, 58], borderColor: colors.rose, backgroundColor: 'rgba(248, 113, 113, 0.2)' }
            ]
        },
        options: getChartDefaults()
    });

    // 4. Carrier SLA
    new Chart(document.getElementById('chart-carrier-sla'), {
        type: 'bar',
        data: {
            labels: ['Amazon Air', 'DHL Express', 'FedEx', 'UPS', 'Regional Freight'],
            datasets: [{
                label: 'On-Time SLA %',
                data: [96.4, 95.2, 94.1, 92.5, 86.2],
                backgroundColor: [colors.emerald, colors.cyan, colors.indigo, colors.amber, colors.rose]
            }]
        },
        options: { ...getChartDefaults(), indexAxis: 'y' }
    });

    // Shipping Cost
    new Chart(document.getElementById('chart-shipping-cost'), {
        type: 'line',
        data: {
            labels: ['Route US-EU', 'Route US-APAC', 'Route EU-APAC', 'Domestic US', 'Domestic EU'],
            datasets: [{
                label: 'Avg Shipping Cost ($ / Order)',
                data: [28.5, 34.2, 31.8, 12.4, 14.1],
                borderColor: colors.amber,
                backgroundColor: 'rgba(251, 191, 36, 0.1)',
                fill: true
            }]
        },
        options: getChartDefaults()
    });

    // 5. Demand Forecast
    const forecastDates = Array.from({length: 30}, (_, i) => `Day ${i+1}`);
    const actualData = [1420, 1450, 1480, 1410, 1510, 1530, 1580, 1600, 1590, 1650, 1680, 1720, 1710, 1750, 1780];
    const predicted = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1780, 1810, 1840, 1860, 1890, 1920, 1950, 1980, 2010, 2040, 2070, 2100, 2130, 2160, 2190, 2220];
    const upperBound = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1780, 1910, 1950, 1980, 2020, 2060, 2100, 2140, 2180, 2220, 2260, 2300, 2340, 2380, 2420, 2460];
    const lowerBound = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1780, 1710, 1730, 1740, 1760, 1780, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980];

    new Chart(document.getElementById('chart-demand-forecast'), {
        type: 'line',
        data: {
            labels: forecastDates,
            datasets: [
                { label: 'Historical Orders', data: actualData, borderColor: colors.cyan, tension: 0.2 },
                { label: 'Holt-Winters Forecast', data: predicted, borderColor: colors.indigo, borderDash: [6, 6], tension: 0.2 },
                { label: '95% Upper Bound', data: upperBound, borderColor: 'rgba(52, 211, 153, 0.5)', borderDash: [2, 2], fill: '+1', backgroundColor: 'rgba(52, 211, 153, 0.08)' },
                { label: '95% Lower Bound', data: lowerBound, borderColor: 'rgba(52, 211, 153, 0.5)', borderDash: [2, 2], fill: false }
            ]
        },
        options: getChartDefaults()
    });

    // 6. Customer RFM Segments
    new Chart(document.getElementById('chart-rfm-segments'), {
        type: 'pie',
        data: {
            labels: ['Champions', 'Loyal Customers', 'Promising', 'At Risk', 'Lost / Churned'],
            datasets: [{
                data: [3200, 4800, 2900, 2500, 1600],
                backgroundColor: [colors.emerald, colors.cyan, colors.indigo, colors.amber, colors.rose]
            }]
        },
        options: getChartDefaults()
    });

    new Chart(document.getElementById('chart-customer-ltv'), {
        type: 'bar',
        data: {
            labels: ['Champions', 'Loyal Customers', 'Promising', 'At Risk', 'Lost'],
            datasets: [{
                label: 'Avg Lifetime Value ($)',
                data: [4250, 2850, 1450, 920, 380],
                backgroundColor: colors.cyan
            }]
        },
        options: getChartDefaults()
    });

    // 7. Waterfall Profit
    new Chart(document.getElementById('chart-waterfall-profit'), {
        type: 'bar',
        data: {
            labels: ['Gross Sales', 'Discounts', 'Net Revenue', 'COGS', 'Shipping Cost', 'Net Profit'],
            datasets: [{
                label: 'Financial Flow ($M)',
                data: [160.0, -17.2, 142.8, -85.2, -11.2, 46.4],
                backgroundColor: [colors.cyan, colors.rose, colors.indigo, colors.rose, colors.amber, colors.emerald]
            }]
        },
        options: getChartDefaults()
    });

    // 8. ABC Pareto
    new Chart(document.getElementById('chart-abc-pareto'), {
        type: 'bar',
        data: {
            labels: ['Class A (Top SKUs)', 'Class B (Mid SKUs)', 'Class C (Tail SKUs)'],
            datasets: [{
                label: 'Revenue Share ($M)',
                data: [114.2, 21.4, 7.2],
                backgroundColor: [colors.cyan, colors.indigo, colors.muted]
            }]
        },
        options: getChartDefaults()
    });

    new Chart(document.getElementById('chart-inventory-doi'), {
        type: 'bar',
        data: {
            labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON'],
            datasets: [{
                label: 'Days of Inventory (DOI)',
                data: [48, 52, 38, 44, 32],
                backgroundColor: colors.purple
            }]
        },
        options: getChartDefaults()
    });

    // 9. Anomalies & Stockout
    new Chart(document.getElementById('chart-anomalies'), {
        type: 'bar',
        data: {
            labels: ['Freight Cost Spikes', 'Margin Compression', 'Defect Outliers', 'Return Surges'],
            datasets: [{
                label: 'Detected Anomaly Count',
                data: [142, 88, 54, 31],
                backgroundColor: colors.rose
            }]
        },
        options: getChartDefaults()
    });

    new Chart(document.getElementById('chart-stockout-risk'), {
        type: 'bar',
        data: {
            labels: ['WH-US-WEST', 'WH-EU-CENTRAL', 'WH-US-EAST', 'WH-APAC-TYO', 'WH-UK-LONDON'],
            datasets: [{
                label: 'Stockout Risk Index (0-1.0)',
                data: [0.18, 0.42, 0.12, 0.28, 0.08],
                backgroundColor: colors.amber
            }]
        },
        options: getChartDefaults()
    });
}

function getChartDefaults() {
    return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { labels: { color: colors.muted, font: { family: 'Inter', size: 11 } } }
        },
        scales: {
            x: { ticks: { color: colors.muted }, grid: { color: colors.gridBorder } },
            y: { ticks: { color: colors.muted }, grid: { color: colors.gridBorder } }
        }
    };
}

function loadExecutiveInsights() {
    const container = document.getElementById('insights-cards-list');
    const sampleInsights = [
        {
            InsightID: 'INS-01',
            Priority: 'CRITICAL',
            Title: 'Inventory Reduction Opportunity at WH-US-WEST',
            Recommendation: 'Current stock level at WH-US-WEST stands at 580,000 units. Reduce holding inventory by 18% to free up ~$420,000 in working capital and lower holding costs.',
            Category: 'Inventory Optimization'
        },
        {
            InsightID: 'INS-02',
            Priority: 'CRITICAL',
            Title: 'Vendor Audit Recommended for Global Supplier 14',
            Recommendation: 'Supplier 14 exhibits a defect rate of 4.25% (Threshold: 1.5%) and average delivery delay of 18 days. Contract renegotiation or vendor replacement recommended.',
            Category: 'Supplier Risk'
        },
        {
            InsightID: 'INS-03',
            Priority: 'HIGH',
            Title: 'Carrier SLA Late Delivery Alert',
            Recommendation: 'Regional Freight Co accounts for 42% of all late shipments. Shift 15% volume to Amazon Air Logistics to boost overall SLA to 97.5%.',
            Category: 'Logistics SLA'
        },
        {
            InsightID: 'INS-04',
            Priority: 'HIGH',
            Title: 'Margin Compression in European Fulfillment Hub',
            Recommendation: 'Net profit margin at WH-EU-CENTRAL is lagging target by 4.2%. Re-evaluate localized freight costs and order fulfillment routes.',
            Category: 'Profitability'
        },
        {
            InsightID: 'INS-05',
            Priority: 'MEDIUM',
            Title: 'Demand Surge in Technology Category',
            Recommendation: 'Technology products generated $54.8M in net revenue. Maintain 30-day safety stock buffer to capture projected peak demand.',
            Category: 'Sales & Demand'
        }
    ];

    container.innerHTML = sampleInsights.map(item => `
        <div class="insight-item">
            <div class="insight-top">
                <span class="insight-tag ${item.Priority}">${item.Priority}</span>
                <span style="font-size: 0.75rem; color: var(--text-muted);">${item.Category}</span>
            </div>
            <div class="insight-title">${item.Title}</div>
            <div class="insight-body">${item.Recommendation}</div>
        </div>
    `).join('');
}
