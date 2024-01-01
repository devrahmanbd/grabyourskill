import subprocess


subprocess.run(['pip', 'install','matplotlib', 'matplotlib-venn'])


import matplotlib.pyplot as plt
from matplotlib_venn import venn2

data_pie = [91.54, 3.2, 1.78, 1.22, 0.93, 0.55]
labels_pie = ["Google", "Bing", "Yandex", "Yahoo!", "Baidu", "DuckDuckGo"]
colors_pie = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

data_bar = [91.54, 3.2, 1.78, 1.22, 0.93, 0.55]  # Use the same data as the pie chart for ranking
labels_bar = ["Google", "Bing", "Yandex", "Yahoo!", "Baidu", "DuckDuckGo"]
colors_bar = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']


rounded_values = [round(value, 2) for value in data_pie]
rounded_values = [int(value * 100) for value in rounded_values]


fig, (ax_pie, ax_bar, ax_venn) = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))


wedges, texts, autotexts = ax_pie.pie(rounded_values, labels=labels_pie, autopct="%1.1f%%", startangle=140, colors=colors_pie, wedgeprops=dict(width=0.3))
ax_pie.set_title("Search Engine Market Share (2023)", fontsize=16, fontweight='bold')
ax_pie.legend(labels_pie, title="Search Engines", loc="center left", bbox_to_anchor=(1, 0.5), prop={'size': 10}, title_fontsize=12)


ax_bar.bar(labels_bar, data_bar, color=colors_bar)
ax_bar.set_ylabel('Search Engine Market Share Ranking')
ax_bar.set_title("Search Engine Market Share (2023)", fontsize=16, fontweight='bold')


venn_labels = {'10': 'Google', '01': 'DuckDuckGo', '11': 'Overlap'}
venn2(subsets=(rounded_values[0], rounded_values[-1], 0), set_labels=('Google', 'DuckDuckGo'), ax=ax_venn, set_colors=('#1f77b4', '#8c564b'), alpha=0.7, subset_label_formatter=lambda x: venn_labels.get(str(x), ''))
ax_venn.set_title("Google vs DuckDuckGo Venn Diagram", fontsize=16, fontweight='bold')


plt.savefig('search_engine_stat.png', bbox_inches='tight')
plt.show()
