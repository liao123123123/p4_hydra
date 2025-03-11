import matplotlib.pyplot as plt

# 创建一个图形和轴
fig, ax = plt.subplots(figsize=(12, 8))

# 隐藏轴
ax.axis('off')

# 定义表格数据
table_data = [
    ["$p$", "::=", "$\\overline{d}$ sinit stele scheck", "Programs"],
    ["$d$", "::=", "", "Declarations"],
    ["", "|", "tele $t$ x := $e$", ""],
    ["", "|", "sensor $t$ x := $e$", ""],
    ["", "|", "header $t$ x", ""],
    ["", "|", "control $t$ x", ""],
    ["$e$", "::=", "", "Expressions"],
    ["", "|", "x", ""],
    ["", "|", "v", ""],
    ["", "|", "$\\oplus(\\overline{e})$", ""],
    ["", "|", "$e_1[e_2]$", ""],
    ["$s$", "::=", "", "Statements"],
    ["", "|", "pass", ""],
    ["", "|", "$s_1;s_2$", ""],
    ["", "|", "x := $e$", ""],
    ["", "|", "if ($e_1$) then $s_1$ else $s_2$", ""],
    ["", "|", "for (x in $e$) s", ""],
    ["", "|", "exn", ""],
    ["$t$", "::=", "bit$\\langle n\\rangle$", "Types"],
    ["", "|", "bool", ""],
    ["", "|", "$t[n]$", ""],
    ["", "|", "set$\\langle t\\rangle$", ""],
    ["", "|", "dict$\\langle t_1, t_2\\rangle$", ""],
    ["$\\oplus$", "::=", "+ | - | * | /", "Operators"],
    ["", "|", "$\\sim$ | \\& | |", ""],
    ["", "|", "== | < | <= | ! | \\&\\& | ||", ""],
    ["", "|", "$\\in$ | $\\notin$", ""],
    ["", "|", "length | push", ""],
    ["$v$", "::=", "$n$", "Values"],
    ["", "|", "$b$", ""],
    ["", "|", "$[\\overline{v}]$", ""],
    ["exn", "::=", "report", "Exceptions"],
    ["", "|", "reject", ""]
]

# 创建表格
table = ax.table(cellText=table_data, cellLoc='left', loc='center')

# 调整表格样式
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# 调整列宽
table.auto_set_column_width([0, 1, 2, 3])

# 保存图形
plt.savefig('syntax_table.png', bbox_inches='tight')

# 显示图形
plt.show()
