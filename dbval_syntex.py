import matplotlib.pyplot as plt

# 创建一个图形和轴
fig, ax = plt.subplots(figsize=(10, 6))

# 隐藏轴
ax.axis('off')

# 定义表格数据
table_data = [
    ["Field f", "::=", "metadata_field | packet_hdr_field"],
    ["Predicate Pred", "::=", "f op v | f in L | Pred & Pred | Pred || Pred | !(Pred)"],
    ["Operator op", "::=", "== | != | < | > | <= | >="],
    ["Value v", "::=", "int | hex | ip-address | true | false"],
    ["Const List L", "::=", "nil | v,L"],
    ["Path P", "::=", ".*S.*"],
    ["Sequence S", "::=", "table | action | table@action | S*S | S^S"],
    ["Assert AT", "::=", "assert(Pred) | assert(P)"],
    ["Filter FT", "::=", "filter(Pred) | filter(P)"],
    ["Assertion A", "::=", "FT ~ AT | AT"]
]

# 创建表格
table = ax.table(cellText=table_data, cellLoc='left', loc='center')

# 调整表格样式
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# 调整列宽
table.auto_set_column_width([0, 1, 2])

# 保存图形
plt.savefig('bnf_table.png', bbox_inches='tight')

# 显示图形
plt.show()
