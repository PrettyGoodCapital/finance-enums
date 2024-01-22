import itertools


US_SECTORS_MAP = {
    'Consumer Discretionary': [
        'Auto Components',
        'Automobiles',
        'Distributors',
        'Diversified Consumer Services',
        'Hotels, Restaurants & Leisure',
        'Household Durables',
        'Internet & Catalog Retail',
        'Leisure Products',
        'Media',
        'Multiline Retail',
        'Specialty Retail',
        'Textiles, Apparel & Luxury Goods'],
    'Consumer Staples': [
        'Beverages',
        'Food & Staples Retailing',
        'Food Products',
        'Household Products',
        'Personal Products',
        'Tobacco'],
    'Energy': [
        'Energy Equipment & Services',
        'Oil, Gas & Consumable Fuels'],
    'Financials': [
        'Banks',
        'Capital Markets',
        'Consumer Finance',
        'Diversified Financial Services',
        'Insurance',
        'Mortgage REITs',
        'Thrifts & Mortgage Finance'],
    'Health Care': [
        'Biotechnology',
        'Health Care Equipment & Supplies',
        'Health Care Providers & Services',
        'Health Care Technology',
        'Life Sciences Tools & Services',
        'Pharmaceuticals'],
    'Industrials': [
        'Aerospace & Defense',
        'Air Freight & Logistics',
        'Airlines',
        'Building Products',
        'Commercial Services & Supplies',
        'Construction & Engineering',
        'Electrical Equipment',
        'Industrial Conglomerates',
        'Machinery',
        'Marine',
        'Professional Services',
        'Road & Rail',
        'Trading Companies & Distributors',
        'Transportation Infrastructure'],
    'Information Technology': [
        'Communications Equipment',
        'Electronic Equipment, Instruments & Components',
        'IT Services',
        'Internet Software & Services',
        'Semiconductors & Semiconductor Equipment',
        'Software',
        'Technology Hardware, Storage & Peripherals'],
    'Materials': [
        'Chemicals',
        'Construction Materials',
        'Containers & Packaging',
        'Metals & Mining',
        'Paper & Forest Products'],
    'Real Estate': [
        'Equity Real Estate Investment Trusts',
        'Real Estate Management & Development'],
    'Telecommunication Services': [
        'Diversified Telecommunication Services',
        'Wireless Telecommunication Services'],
    'Utilities': [
        'Electric Utilities',
        'Gas Utilities',
        'Independent Power and Renewable Electricity Producers',
        'Multi-Utilities',
        'Water Utilities ']
}

US_SECTORS = set(US_SECTORS_MAP.keys())
US_INDUSTRIES = set(itertools.chain(*US_SECTORS_MAP.values()))
