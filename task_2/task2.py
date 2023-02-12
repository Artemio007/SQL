import sqlite3
from less31.homework.task_3.task3 import concat

connect_db = sqlite3.connect('material.db')
cursor_db = connect_db.cursor()
cursor_db.execute("""CREATE TABLE IF NOT EXISTS material(
    material_id INT PRIMARY KEY,
    weight REAL,
    height REAL,
    info VARCHAR(50));
""")
connect_db.commit()

material_ = (1, 50, 10, 'it is iron (not man)')
material_1 = (2, 30, 90, "[('wheels', 4), ('passengers', 5)]")
all_what_i_want = [
    (3, 34, 12, '[("Metals", 6), ("N/A", 4)]'),
    (4, 455, 23, '[("Wood", 7), ("N/A", 3)]'),
    (5, 547, 14, '[("Paper", 8), ("N/A", 2)]'),
    (6, 457, 15, '[("Natural Textiles", 9), ("N/A", 6)]'),
    (7, 78, 36, '[("Synthetic Textiles", 5), ("N/A", 7)]'),
    (8, 97, 47, '[("Leather", 4), ("N/A", 9)]'),
    (9, 678, 58, '[("Fibers", 7), ("N/A", 8)]'),
    (10, 57, 69, '[("Stone", 9), ("N/A", 7)]'),
    (11, 8, 36, '[("topsoil", 0), ("N/A", 6)]'),
    (12, 568, 69, '[("rock", 5), ("N/A", 4)]'),
]
# cursor_db.execute("INSERT INTO material VALUES(?, ?, ?, ?);", material_)
# connect_db.commit()
# cursor_db.execute("INSERT INTO material VALUES(?, ?, ?, ?);", material_1)
# connect_db.commit()
# cursor_db.executemany("INSERT INTO material VALUES(?, ?, ?, ?);", all_what_i_want)
# connect_db.commit()
mat = cursor_db.execute("SELECT info FROM material WHERE material_id = 2").fetchone()
mat1 = cursor_db.execute("SELECT info FROM material WHERE material_id = 2").fetchone()
mat2= cursor_db.execute("SELECT info FROM material WHERE material_id = 2").fetchone()
mat3 = cursor_db.execute("SELECT info FROM material WHERE material_id = 2").fetchone()
mat4 = cursor_db.execute("SELECT info FROM material WHERE material_id = 2").fetchone()
# print(mat[0])

print(concat(mat, mat2, mat2, mat3, mat4))
print(type(concat(mat, mat2, mat2, mat3, mat4)))