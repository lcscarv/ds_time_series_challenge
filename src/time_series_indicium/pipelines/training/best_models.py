import json

best_models_dict = {'ASEAN-5': 'RWD',
 'Advanced economies': 'SESOpt',
 'Afghanistan': 'AutoETS',
 'Africa (Region)': 'RWD',
 'Albania': 'HistoricAverage',
 'Algeria': 'AutoETS',
 'Andorra': 'RWD',
 'Angola': 'RWD',
 'Antigua and Barbuda': 'HistoricAverage',
 'Argentina': 'HistoricAverage',
 'Armenia': 'HistoricAverage',
 'Aruba': 'RWD',
 'Asia and Pacific': 'RWD',
 'Australia': 'RWD',
 'Australia and New Zealand': 'RWD',
 'Austria': 'AutoARIMA',
 'Azerbaijan': 'RWD',
 'Bahrain': 'RWD',
 'Bangladesh': 'AutoETS',
 'Barbados': 'AutoETS',
 'Belarus': 'RWD',
 'Belgium': 'SESOpt',
 'Belize': 'RWD',
 'Benin': 'SESOpt',
 'Bhutan': 'AutoARIMA',
 'Bolivia': 'AutoETS',
 'Bosnia and Herzegovina': 'AutoETS',
 'Botswana': 'SESOpt',
 'Brazil': 'SESOpt',
 'Brunei Darussalam': 'RWD',
 'Bulgaria': 'AutoETS',
 'Burkina Faso': 'SESOpt',
 'Burundi': 'RWD',
 'Cabo Verde': 'HistoricAverage',
 'Cambodia': 'HistoricAverage',
 'Cameroon': 'SESOpt',
 'Canada': 'RWD',
 'Caribbean': 'HistoricAverage',
 'Central African Republic': 'RWD',
 'Central America': 'RWD',
 'Central Asia and the Caucasus': 'RWD',
 'Chad': 'RWD',
 'Chile': 'SESOpt',
 'China': 'AutoETS',
 'Colombia': 'AutoARIMA',
 'Comoros': 'HistoricAverage',
 'Costa Rica': 'SESOpt',
 'Croatia': 'AutoETS',
 'Cyprus': 'AutoETS',
 'Czech Republic': 'HistoricAverage',
 "Côte d'Ivoire": 'SESOpt',
 'Democratic Republic of the Congo': 'RWD',
 'Denmark': 'AutoARIMA',
 'Djibouti': 'RWD',
 'Dominica': 'HistoricAverage',
 'Dominican Republic': 'SESOpt',
 'East Asia': 'AutoARIMA',
 'Eastern Europe ': 'HistoricAverage',
 'Ecuador': 'RWD',
 'Egypt': 'HistoricAverage',
 'El Salvador': 'AutoETS',
 'Emerging and Developing Asia': 'SESOpt',
 'Emerging and Developing Europe': 'HistoricAverage',
 'Emerging market and developing economies': 'SESOpt',
 'Equatorial Guinea': 'AutoARIMA',
 'Eritrea': 'RWD',
 'Estonia': 'SESOpt',
 'Eswatini': 'SESOpt',
 'Ethiopia': 'RWD',
 'Euro area': 'AutoARIMA',
 'Europe': 'AutoARIMA',
 'European Union': 'SESOpt',
 'Fiji': 'AutoETS',
 'Finland': 'SESOpt',
 'France': 'HistoricAverage',
 'Gabon': 'RWD',
 'Georgia': 'RWD',
 'Germany': 'AutoARIMA',
 'Ghana': 'HistoricAverage',
 'Greece': 'HistoricAverage',
 'Grenada': 'RWD',
 'Guatemala': 'AutoETS',
 'Guinea': 'SESOpt',
 'Guinea-Bissau': 'RWD',
 'Guyana': 'HistoricAverage',
 'Haiti': 'HistoricAverage',
 'Honduras': 'RWD',
 'Hong Kong SAR': 'RWD',
 'Hungary': 'AutoETS',
 'Iceland': 'RWD',
 'India': 'HistoricAverage',
 'Indonesia': 'HistoricAverage',
 'Iran': 'SESOpt',
 'Iraq': 'RWD',
 'Ireland': 'HistoricAverage',
 'Israel': 'SESOpt',
 'Italy': 'HistoricAverage',
 'Jamaica': 'SESOpt',
 'Japan': 'SESOpt',
 'Jordan': 'SESOpt',
 'Kazakhstan': 'HistoricAverage',
 'Kenya': 'RWD',
 'Kiribati': 'RWD',
 'Korea': 'AutoARIMA',
 'Kosovo': 'AutoARIMA',
 'Kuwait': 'HistoricAverage',
 'Kyrgyz Republic': 'RWD',
 'Lao P.D.R.': 'RWD',
 'Latin America and the Caribbean': 'AutoARIMA',
 'Latvia': 'SESOpt',
 'Lebanon': 'SESOpt',
 'Lesotho': 'AutoARIMA',
 'Liberia': 'RWD',
 'Libya': 'SESOpt',
 'Lithuania': 'AutoARIMA',
 'Luxembourg': 'AutoETS',
 'Macao SAR': 'SESOpt',
 'Madagascar': 'RWD',
 'Major advanced economies (G7)': 'AutoETS',
 'Malawi': 'SESOpt',
 'Malaysia': 'RWD',
 'Maldives': 'RWD',
 'Mali': 'RWD',
 'Malta': 'RWD',
 'Marshall Islands': 'SESOpt',
 'Mauritania': 'RWD',
 'Mauritius': 'AutoETS',
 'Mexico': 'SESOpt',
 'Micronesia': 'SESOpt',
 'Middle East (Region)': 'RWD',
 'Middle East and Central Asia': 'SESOpt',
 'Moldova': 'RWD',
 'Mongolia': 'HistoricAverage',
 'Montenegro': 'SESOpt',
 'Morocco': 'AutoARIMA',
 'Mozambique': 'RWD',
 'Myanmar': 'RWD',
 'Namibia': 'RWD',
 'Nauru': 'RWD',
 'Nepal': 'RWD',
 'New Zealand': 'HistoricAverage',
 'Nicaragua': 'SESOpt',
 'Niger': 'RWD',
 'Nigeria': 'SESOpt',
 'North Africa': 'RWD',
 'North America': 'SESOpt',
 'North Macedonia': 'HistoricAverage',
 'Norway': 'AutoARIMA',
 'Oman': 'AutoARIMA',
 'Other advanced economies': 'SESOpt',
 'Pacific Islands ': 'HistoricAverage',
 'Pakistan': 'HistoricAverage',
 'Palau': 'AutoARIMA',
 'Panama': 'SESOpt',
 'Papua New Guinea': 'HistoricAverage',
 'Paraguay': 'AutoETS',
 'Peru': 'SESOpt',
 'Philippines': 'RWD',
 'Poland': 'AutoARIMA',
 'Portugal': 'SESOpt',
 'Puerto Rico': 'RWD',
 'Qatar': 'RWD',
 'Republic of Congo': 'RWD',
 'Romania': 'AutoETS',
 'Russia': 'HistoricAverage',
 'Rwanda': 'RWD',
 'Saint Kitts and Nevis': 'AutoETS',
 'Saint Lucia': 'AutoARIMA',
 'Saint Vincent and the Grenadines': 'SESOpt',
 'Samoa': 'HistoricAverage',
 'San Marino': 'RWD',
 'Saudi Arabia': 'RWD',
 'Senegal': 'AutoARIMA',
 'Serbia': 'AutoETS',
 'Seychelles': 'AutoETS',
 'Sierra Leone': 'RWD',
 'Singapore': 'AutoETS',
 'Slovak Republic': 'AutoARIMA',
 'Slovenia': 'SESOpt',
 'Solomon Islands': 'RWD',
 'Somalia': 'RWD',
 'South Africa': 'AutoETS',
 'South America': 'HistoricAverage',
 'South Asia': 'HistoricAverage',
 'South Sudan': 'RWD',
 'Southeast Asia': 'AutoARIMA',
 'Spain': 'RWD',
 'Sri Lanka': 'HistoricAverage',
 'Sub-Saharan Africa': 'RWD',
 'Sub-Saharan Africa (Region) ': 'RWD',
 'Sudan': 'HistoricAverage',
 'Suriname': 'RWD',
 'Sweden': 'AutoETS',
 'Switzerland': 'SESOpt',
 'Syria': 'RWD',
 'São Tomé and Príncipe': 'SESOpt',
 'Taiwan Province of China': 'AutoETS',
 'Tajikistan': 'HistoricAverage',
 'Tanzania': 'RWD',
 'Thailand': 'AutoARIMA',
 'The Bahamas': 'SESOpt',
 'The Gambia': 'RWD',
 'The Netherlands': 'AutoARIMA',
 'Timor-Leste': 'AutoETS',
 'Togo': 'RWD',
 'Tonga': 'RWD',
 'Trinidad and Tobago': 'AutoETS',
 'Tunisia': 'AutoETS',
 'Turkmenistan': 'SESOpt',
 'Tuvalu': 'AutoETS',
 'Türkiye': 'RWD',
 'Uganda': 'RWD',
 'Ukraine': 'AutoARIMA',
 'United Arab Emirates': 'RWD',
 'United Kingdom': 'AutoARIMA',
 'United States': 'RWD',
 'Uruguay': 'HistoricAverage',
 'Uzbekistan': 'AutoETS',
 'Vanuatu': 'RWD',
 'Venezuela': 'SESOpt',
 'Vietnam': 'RWD',
 'West Bank and Gaza': 'SESOpt',
 'Western Europe': 'AutoARIMA',
 'Western Hemisphere (Region)': 'AutoARIMA',
 'World': 'SESOpt',
 'Yemen': 'HistoricAverage',
 'Zambia': 'RWD',
 'Zimbabwe': 'SESOpt'}

with open("json_files/best_models.json", "w") as outfile:
    json.dump(best_models_dict, outfile)
    