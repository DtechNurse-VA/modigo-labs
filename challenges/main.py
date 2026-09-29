def merge_tags(tags1, tags2):
   # mrs = ('tags2')
    merged = set(tags1) | set(tags2)
    #mrs.append(merged)
    return merged

print(merge_tags({'python', 'web'}, {'web', 'css' }))