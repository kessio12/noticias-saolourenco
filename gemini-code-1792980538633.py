idx_news_array = html.find('const noticiasPadrao = [')
idx_news_end = html.find('];', idx_news_array)
print(html[idx_news_array:idx_news_end+2])