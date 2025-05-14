import re
n = int(input())
adj = {}
search_link = re.compile(r'<A HREF="([^"]+)">')

def addlink(src,dest,graph):
    # print(graph)
    graph.setdefault(src,[]).append(dest)

for i in range(n):
    content = ""
    src_url = input()
    while True:
        cur_line = input()
        if cur_line == r"</HTML>":
            break
        content += cur_line
    links = search_link.findall(content)
    for link in links:
        addlink(src_url,link,adj)

print(adj)
for src_url,dest_urls in adj.items():
    for dest_url in dest_urls:
        print("Link from "+ src_url + " to "+dest_url)


def dfs(node,dest,vis):
    if node not in vis:
        vis.add(node)

        if node == dest:
            return True
        else:
            for i in adj.get(node,[]):
                if dfs(i,dest,vis):
                    return True
while True:
    src = input()
    if src == "The End":
        break
    dest = input()

    if dfs(src,dest,set()):
        print("Can surf from " + src + " to "+ dest+".")
    else:
        print("Can't surf from " + src + " to "+ dest+".")










# for i in range(n):
#     current_page = input()

