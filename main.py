from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {
        "message" : "Chào mừng đến với FastAPI"
    }
    
@app.get("/students")
def get_students():
    print ("Lấy danh sách sinh viên nhe cha.")
    return [{"id": 1, "name": "Nguyễn Văn A"}]

@app.post("/students")
def create_student ():
    print ("Thêm mới sinh viên")
    return {
        "message": "Thêm mới thành công"
    }
    
@app.put ("/students/{student_id}")
def update_student (student_id: int):
    print (f"Cập nhật sinh viên có id là {student_id}")
    return {
        f"Đã cập nhật có {student_id}"
    }
    
@app.patch ("/students.{student_id}")
def patch_student (student_id):
    print (f"Đã cập nhật một phần dữ liệu")
    return {
        f"Đã cập nhật phần nhỏ có {student_id}"
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    print (f"Đã xóa {student_id}")
    return {f" đã xóa   "}


