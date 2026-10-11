from flask import Flask, jsonify, request, url_for, make_response
from markupsafe import escape

app = Flask(__name__)

app.json.ensure_ascii = False

STUDENTS = {
    "23T1020001": {
        "name": "Nguyễn Văn An",
        "lop": "K47A",
        "scores": {"PMMNM": 8.5, "CSDL": 7.0, "MMT": 9.0}
    },
    "23T1020002": {
        "name": "Trần Thị Bình",
        "lop": "K47A",
        "scores": {"PMMNM": 6.0, "CSDL": 5.5, "MMT": 7.0}
    },
    "23T1020003": {
        "name": "Lê Hoàng Cường",
        "lop": "K47B",
        "scores": {"PMMNM": 9.5, "CSDL": 9.0}
    },
    "23T1020004": {
        "name": "Phạm Minh Dũng",
        "lop": "K47B",
        "scores": {"PMMNM": 4.0, "CSDL": 3.5, "MMT": 5.0}
    },
    "23T1020005": {
        "name": "Hoàng Thu Hà",
        "lop": "K47A",
        "scores": {}
    },
    "23T1020006": {
        "name": "Vũ Quốc Khánh",
        "lop": "K47C",
        "scores": {"PMMNM": 7.5, "MMT": 8.0}
    }
}

def calculate_grade(scores):
    if not scores:
        return "-", "-"
    
    gpa_mon = []
    for diem in scores.values():
        if diem >= 8.5:
            gpa_mon.append(4.0)
        elif diem >= 7.0:
            gpa_mon.append(3.0)
        elif diem >= 5.5:
            gpa_mon.append(2.0)
        elif diem >= 4.0:
            gpa_mon.append(1.0)
        else:
            gpa_mon.append(0.0)

    diem_tb = round(sum(gpa_mon) / len(gpa_mon), 2)
    
    if diem_tb >= 3.60:
        loai = "Xuất sắc"
    elif diem_tb >= 3.20:
        loai = "Giỏi"
    elif diem_tb >= 2.50:
        loai = "Khá"
    elif diem_tb >= 2.00:
        loai = "Trung bình"
    elif diem_tb >= 1.00:
        loai = "Yếu"
    else:
        loai = "Kém"
        
    return diem_tb, loai

@app.route('/api/students')
def api_students():
    return jsonify(STUDENTS)

# Câu 1
@app.route('/')
def home():
    tong_sv = len(STUDENTS)
    
    danh_sach_lop = []
    for info in STUDENTS.values():
        if info['lop'] not in danh_sach_lop:
            danh_sach_lop.append(info['lop'])
    danh_sach_lop.sort()
    
    tong_so_lop = len(danh_sach_lop)
    chuoi_lop = ", ".join(danh_sach_lop)
    
    return f"""
    <h1>Trang chủ quản lý sinh viên</h1>
    <p><b>Tổng số sinh viên:</b> {tong_sv}</p>
    <p><b>Số lớp:</b> {tong_so_lop} ({chuoi_lop})</p>
    <ul>
        <li><a href="{url_for('student_list')}">Danh sách sinh viên (/students)</a></li>
        <li><a href="{url_for('api_students')}">API Sinh viên (/api/students)</a></li>
    </ul>
    """

# Câu 2
@app.route('/students')
def student_list():
    selected_class = request.args.get('lop', '')
    
    all_classes = []
    for info in STUDENTS.values():
        if info['lop'] not in all_classes:
            all_classes.append(info['lop'])
    all_classes.sort()
    
    filter_links = [f'<a href="{url_for("student_list")}">Tất cả</a>']
    for c in all_classes:
        filter_links.append(f'<a href="{url_for("student_list", lop=c)}">{c}</a>')
    filter_html = ' | '.join(filter_links)
    
    filtered_students = {}
    for mssv, info in STUDENTS.items():
        if selected_class == '' or info['lop'].lower() == selected_class.lower():
            filtered_students[mssv] = info
            
    if len(filtered_students) > 0:
        table_rows = ""
        for mssv, info in filtered_students.items():
            avg, loai = calculate_grade(info['scores'])
            table_rows += f"""
            <tr>
                <td><a href="/students/{mssv}">{escape(mssv)}</a></td>
                <td>{escape(info['name'])}</td>
                <td>{escape(info['lop'])}</td>
                <td>{avg}</td>
                <td>{loai}</td>
            </tr>
            """
        table_html = f"""
        <table border="1" cellpadding="8" cellspacing="0">
            <thead>
                <tr>
                    <th>MSSV</th>
                    <th>Họ tên</th>
                    <th>Lớp</th>
                    <th>Điểm TB</th>
                    <th>Xếp loại</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        """
    else:
        table_html = "<p>Không có sinh viên phù hợp.</p>"

    return f"""
    <h2>Danh sách sinh viên</h2>
    <p><b>Lọc theo lớp:</b> {filter_html}</p>
    {table_html}
    <br><a href="{url_for('home')}">Quay lại Trang chủ</a>
    """

# Câu 3: Trang chi tiết sinh viên /students/<mssv>
@app.route('/students/<mssv>')
def student_detail(mssv):

    if mssv not in STUDENTS:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")
    
    student = STUDENTS[mssv]
    avg, loai = calculate_grade(student['scores'])
    
    if student['scores']:
        score_rows = ""
        for mon, diem in student['scores'].items():
            score_rows += f"""
            <tr>
                <td>{mon}</td>
                <td>{diem}</td>
            </tr>
            """
        score_table = f"""
        <table border="1" cellpadding="6" cellspacing="0">
            <thead>
                <tr>
                    <th>Môn học</th>
                    <th>Điểm</th>
                </tr>
            </thead>
            <tbody>
                {score_rows}
            </tbody>
        </table>
        """
    else:
        score_table = "<p>Chưa có điểm học phần nào.</p>"
    
    class_link = f'<a href="{url_for("student_list", lop=student["lop"])}">{student["lop"]}</a>'
    
    return f"""
    <h2>Chi tiết sinh viên: {student['name']}</h2>
    <p><b>MSSV:</b> {mssv}</p>
    <p><b>Lớp:</b> {class_link}</p>
    <p><b>Điểm TB (Hệ 4):</b> {avg}</p>
    <p><b>Xếp loại:</b> {loai}</p>
    
    <h3>Bảng điểm từng học phần</h3>
    {score_table}
    
    <br><br>
    <a href="{url_for('student_list')}">Quay lại Danh sách sinh viên</a>
    """

# Câu 4: Link rút gọn /sv/<mssv> chuyển hướng 301 sang /students/<mssv>
@app.route('/sv/<mssv>')
def redirect_student(mssv):
    return redirect(url_for('student_detail', mssv=mssv), code=301)

# Câu 5: Xuất bảng điểm CSV /students/<mssv>/export
@app.route('/students/<mssv>/export')
def export_csv(mssv):
    if mssv not in STUDENTS:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")
        
    student = STUDENTS[mssv]
    
    csv_lines = ["hoc_phan,diem"]
    for mon, diem in student['scores'].items():
        csv_lines.append(f"{mon},{diem}")
        
    csv_content = "\n".join(csv_lines)
    
    response = make_response(csv_content)
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    response.headers['Content-Disposition'] = f'attachment; filename=diem_{mssv}.csv'
    
    return response

# Câu 6: Tìm kiếm an toàn /search?q=...
@app.route('/search')
def search_student():
    query = request.args.get('q', '').strip()
    
    # Escape từ khóa để chống lỗi XSS cả ở thuộc tính value và văn bản hiển thị
    escaped_query = escape(query)
    
    results = {}
    if query:
        q_lower = query.lower()
        for mssv, info in STUDENTS.items():
            # Tìm kiếm theo họ tên HOẶC mssv (không phân biệt hoa thường)
            if q_lower in info['name'].lower() or q_lower in mssv.lower():
                results[mssv] = info

    # Xây dựng giao diện danh sách kết quả
    if query:
        result_header = f'<p>Tìm thấy <b>{len(results)}</b> kết quả cho "<b>{escaped_query}</b>"</p>'
        if results:
            items = ""
            for mssv, info in results.items():
                items += f'<li><a href="{url_for("student_detail", mssv=mssv)}">{escape(info["name"])} ({escape(mssv)}) - Lớp {escape(info["lop"])}</a></li>'
            result_html = f"<ul>{items}</ul>"
        else:
            result_html = "<p>Không tìm thấy sinh viên nào.</p>"
    else:
        result_header = ""
        result_html = ""

    return f"""
    <h2>Tìm kiếm sinh viên</h2>
    <form action="{url_for('search_student')}" method="GET">
        <input type="text" name="q" value="{escaped_query}" placeholder="Nhập tên hoặc MSSV...">
        <button type="submit">Tìm kiếm</button>
    </form>
    {result_header}
    {result_html}
    <br><a href="{url_for('home')}">Quay lại Trang chủ</a>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8000)