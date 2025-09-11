from datetime import datetime
import sqlite3
import dsCrypto

DS_TEST_DB = "dsTestDB.db"
DS_SUBJECT_HEADER = ['subject_id', '이름', '생년월일', '성별']
DS_TEST_ID_HEADER = ['subject_id', '이름', '생년월일', '성별', '검사일시', '점수',\
                     '정답1', '응답1', '정답2', '응답2', '정답3', '응답3', '정답4', '응답4',\
                     '정답5', '응답5', '정답6', '응답6', '정답7', '응답7', '정답8', '응답8', \
                     '정답9', '응답9', '정답10', '응답10', '정답11', '응답11', '정답12', '응답12']

# 환자(검사 대상자)를 위한 테이블
def createTableSubject():
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "create table if not exists DS_TEST_SUBJECT(\
        SUBJECT_ID integer primary key autoincrement not null,\
        SUBJECT_NAME text,\
        BIRTH_DATE text,\
        GENDER text)"
    cur.execute(query)
    con.commit()
    con.close()

def checkTableSuject(text_name, text_birth_date, text_gender):
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    # querydata = (text_name, text_birth_date, text_gender)
    en_text_name = dsCrypto.encryptMessage(text_name)
    en_text_birth_date = dsCrypto.encryptMessage(text_birth_date)
    en_text_gender = dsCrypto.encryptMessage(text_gender)
    querydata = (en_text_name, en_text_birth_date, en_text_gender)

    query = "select exists(select 1 from DS_TEST_SUBJECT where SUBJECT_NAME=? AND BIRTH_DATE=? and GENDER=?)"
    cur.execute(query, querydata)
    is_exist = cur.fetchone()[0] # 있으면 1, 없으면 0
    con.commit()
    con.close()
    print(is_exist)
    if is_exist:
        print("있음")
        return True
    else:
        print("없음")
        return False

def insertTableSubject(text_name, text_birth_date, text_gender):
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    # querydata = (text_name, text_birth_date, text_gender)
    en_text_name = dsCrypto.encryptMessage(text_name)
    en_text_birth_date = dsCrypto.encryptMessage(text_birth_date)
    en_text_gender = dsCrypto.encryptMessage(text_gender)
    querydata = (en_text_name, en_text_birth_date, en_text_gender)

    query = "insert into DS_TEST_SUBJECT(SUBJECT_NAME, BIRTH_DATE, GENDER) values(?, ?, ?)" 
    cur.execute(query, querydata)
    con.commit()
    con.close()

def deleteTableSubject(text_name, text_birth_date, text_gender):
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    # querydata = (text_name, text_birth_date, text_gender)
    en_text_name = dsCrypto.encryptMessage(text_name)
    en_text_birth_date = dsCrypto.encryptMessage(text_birth_date)
    en_text_gender = dsCrypto.encryptMessage(text_gender)
    querydata = (en_text_name, en_text_birth_date, en_text_gender)

    query = "delete from DS_TEST_SUBJECT where (SUBJECT_NAME=? and BIRTH_DATE=? and GENDER=?)" 
    cur.execute(query, querydata)
    con.commit()
    con.close()

def selectTableSubject():
    datas = [DS_SUBJECT_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "select * from DS_TEST_SUBJECT"
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender in data:
        # datas.append([id, name, birth_date, gender])
        de_name = dsCrypto.decryptMessage(name)
        de_birth_date = dsCrypto.decryptMessage(birth_date)
        de_gender = dsCrypto.decryptMessage(gender)
        datas.append([id, de_name, de_birth_date, de_gender])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableSubjectRaw():
    datas = [DS_SUBJECT_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "select * from DS_TEST_SUBJECT"
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender in data:
        datas.append([id, name, birth_date, gender])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableSubjectByName(text_name):
    datas = [DS_SUBJECT_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    en_text_name = dsCrypto.encryptMessage(text_name) # 암호화
    query = "select * from DS_TEST_SUBJECT where SUBJECT_NAME='%s'" % en_text_name
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender in data:
        # datas.append((id, name, birth_date, gender))
        de_name = dsCrypto.decryptMessage(name)
        de_birth_date = dsCrypto.decryptMessage(birth_date)
        de_gender = dsCrypto.decryptMessage(gender)
        datas.append([id, de_name, de_birth_date, de_gender])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableSubjectByBirthDate(text_birth_date):
    datas = [DS_SUBJECT_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    en_text_birth_date = dsCrypto.encryptMessage(text_birth_date) # 암호화
    query = "select * from DS_TEST_SUBJECT where BIRTH_DATE='%s'" % en_text_birth_date
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender in data:
        # datas.append((id, name, birth_date, gender))
        de_name = dsCrypto.decryptMessage(name)
        de_birth_date = dsCrypto.decryptMessage(birth_date)
        de_gender = dsCrypto.decryptMessage(gender)
        datas.append([id, de_name, de_birth_date, de_gender])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableSubjectKeywords(text_name="", text_birth_date=""):
    datas = [DS_SUBJECT_HEADER]
    if text_name == "" and text_birth_date == "":
        return datas
    elif text_name == "":
        return selectTableSubjectByBirthDate(text_birth_date)
    elif text_birth_date == "":
        return selectTableSubjectByName(text_name)
    else:
        return datas

# [['문항', '정답', '선택', '정답여부', '응답(주관식)', '정답여부(주관식)'], 
# [1, '장미', '장미', 1, '주관식X', 0], 
# [2, '커피', '사과', 0, '주관식X', 0], 
# [3, '화장품', '화장품', 1, '주관식X', 0], 
# [4, '생강', '레몬', 0, '주관식X', 0], 
# [5, '딸기', '딸기', 1, '주관식X', 0], 
# [6, '녹차', '녹차', 1, '주관식X', 0], 
# [7, '재/연기', '바나나', 0, '주관식X', 0], 
# [8, '허브', '버섯', 0, '주관식X', 0], 
# [9, '멜론', '멜론', 1, '주관식X', 0], 
# [10, '나무', '나무', 1, '주관식X', 0], 
# [11, '비누', '비누', 1, '주관식X', 0], 
# [12, '초콜릿', '숯불고기', 0, '주관식X', 0]]

# 인지지검사 정보를 위한 테이블
def createTableTestID():
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "create table if not exists DS_TEST_ID(\
        SUBJECT_ID integer primary key,\
        SUBJECT_NAME text,\
        BIRTH_DATE text,\
        GENDER text,\
        TEST_DATETIME text,\
        TEST_SCORE int,\
        ANSWER_01 text,\
        CHOICE_01 text,\
        ANSWER_02 text,\
        CHOICE_02 text,\
        ANSWER_03 text,\
        CHOICE_03 text,\
        ANSWER_04 text,\
        CHOICE_04 text,\
        ANSWER_05 text,\
        CHOICE_05 text,\
        ANSWER_06 text,\
        CHOICE_06 text,\
        ANSWER_07 text,\
        CHOICE_07 text,\
        ANSWER_08 text,\
        CHOICE_08 text,\
        ANSWER_09 text,\
        CHOICE_09 text,\
        ANSWER_10 text,\
        CHOICE_10 text,\
        ANSWER_11 text,\
        CHOICE_11 text,\
        ANSWER_12 text,\
        CHOICE_12 text)"
    cur.execute(query)
    con.commit()
    con.close()
    
def insertTableTestID(name, birth_date, gender, test_date_time, test_score,\
            answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
            answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
            answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12):
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    
    # querydata = (name, birth_date, gender, test_date_time, test_score,\
    #         answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
    #         answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
    #         answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12)
    en_name = dsCrypto.encryptMessage(name)
    en_birth_date = dsCrypto.encryptMessage(birth_date)
    en_gender = dsCrypto.encryptMessage(gender)
    querydata = (en_name, en_birth_date, en_gender, test_date_time, test_score,\
            answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
            answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
            answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12)
        
    query = "insert into DS_TEST_ID(SUBJECT_NAME, BIRTH_DATE, GENDER, TEST_DATETIME, TEST_SCORE, \
        ANSWER_01, CHOICE_01, ANSWER_02, CHOICE_02, ANSWER_03, CHOICE_03, ANSWER_04, CHOICE_04, \
        ANSWER_05, CHOICE_05, ANSWER_06, CHOICE_06, ANSWER_07, CHOICE_07, ANSWER_08, CHOICE_08, \
        ANSWER_09, CHOICE_09, ANSWER_10, CHOICE_10, ANSWER_11, CHOICE_11, ANSWER_12, CHOICE_12) \
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" 
    cur.execute(query, querydata)
    con.commit()
    con.close()
    
def selectTableTestID():
    print("selectTableTestID")
    datas = [DS_TEST_ID_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "select * from DS_TEST_ID"
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender, test_date_time, test_score,\
        answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
        answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
        answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12 in data:
        
        de_name = dsCrypto.decryptMessage(name)
        de_birth_date = dsCrypto.decryptMessage(birth_date)
        de_gender = dsCrypto.decryptMessage(gender)
        
        datas.append([id, de_name, de_birth_date, de_gender, test_date_time, test_score,\
                    answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04, \
                    answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08, \
                    answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableTestIDRaw():
    print("selectTableTestID")
    datas = [DS_TEST_ID_HEADER]
    con = sqlite3.connect(DS_TEST_DB)
    cur = con.cursor()
    query = "select * from DS_TEST_ID"
    cur.execute(query)
    data = cur.fetchall()
    # print("select data:", data)
    for id, name, birth_date, gender, test_date_time, test_score,\
        answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
        answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
        answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12 in data:
        datas.append([id, name, birth_date, gender, test_date_time, test_score,\
                    answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04, \
                    answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08, \
                    answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12])
    con.commit()
    con.close()
    print("select datas:", datas)
    return datas

def selectTableTestIDKeywords(text_name="", text_birth_date="", text_gender=""):
    print("selectTableTestIDKeywords: %s, %s, %s" % (text_name, text_birth_date, text_gender))
    datas = [DS_TEST_ID_HEADER]
    if text_name == "" or text_birth_date == "" or text_gender == "":
        return datas
    else:
        con = sqlite3.connect(DS_TEST_DB)
        cur = con.cursor()
        query = "select * from DS_TEST_ID where SUBJECT_NAME=? and BIRTH_DATE=? and GENDER=?"
        # query_data = (text_name, text_birth_date, text_gender)
        print(text_name, text_birth_date, text_gender)

        en_text_name = dsCrypto.encryptMessage(text_name)
        en_text_birth_date = dsCrypto.encryptMessage(text_birth_date)
        en_text_gender = dsCrypto.encryptMessage(text_gender)
        
        print(en_text_name, en_text_birth_date, en_text_gender)

        query_data = (en_text_name, en_text_birth_date, en_text_gender)
        cur.execute(query, query_data)
        data = cur.fetchall()
        print("select data:", data)
        for id, name, birth_date, gender, test_date_time, test_score,\
            answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
            answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
            answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12 in data:
            
            de_name = dsCrypto.decryptMessage(name)
            de_birth_date = dsCrypto.decryptMessage(birth_date)
            de_gender = dsCrypto.decryptMessage(gender)
            
            datas.append([id, de_name, de_birth_date, de_gender, test_date_time, test_score,\
                    answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04, \
                    answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08, \
                    answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12])
        con.commit()
        con.close()
        print("select datas:", datas)
        return datas
    
def selectTableTestIDOne(text_name="", text_birth_date="", text_gender="", text_date_time =""):
    datas = []
    if text_name == "" or text_birth_date == "" or text_gender == "" or text_date_time == "":
        return datas
    else:
        con = sqlite3.connect(DS_TEST_DB)
        cur = con.cursor()
        query = "select * from DS_TEST_ID where (SUBJECT_NAME=? and BIRTH_DATE=? and GENDER=? and TEST_DATETIME=?) limit 1"
        # query_data = (text_name, text_birth_date, text_gender, text_date_time)
        # query_data = (text_name, text_birth_date, text_gender)
        en_text_name = dsCrypto.encryptMessage(text_name)
        en_text_birth_date = dsCrypto.encryptMessage(text_birth_date)
        en_text_gender = dsCrypto.encryptMessage(text_gender)
        query_data = (en_text_name, en_text_birth_date, en_text_gender, text_date_time)

        cur.execute(query, query_data)
        data = cur.fetchall()
        # datas = list(data) # Tuple --> List # 변환시 오류 잘 난다.
        for id, name, birth_date, gender, test_date_time, test_score,\
            answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04,\
            answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08,\
            answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12 in data:
            
            de_name = dsCrypto.decryptMessage(name)
            de_birth_date = dsCrypto.decryptMessage(birth_date)
            de_gender = dsCrypto.decryptMessage(gender)
            
            datas.append([id, de_name, de_birth_date, de_gender, test_date_time, test_score,\
                    answer_01, choice_01, answer_02, choice_02, answer_03, choice_03, answer_04, choice_04, \
                    answer_05, choice_05, answer_06, choice_06, answer_07, choice_07, answer_08, choice_08, \
                    answer_09, choice_09, answer_10, choice_10, answer_11, choice_11, answer_12, choice_12])
        
        con.commit()
        con.close()
        print("selectTableTestIDOne:", datas)
        return datas


if __name__ == "__main__":
    # createTableSubject()
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    # insertTableSubject("최종우", "1952-08-22", "남성")
    # insertTableSubject("홍길동", "1942-10-29", "여성")
    # insertTableSubject("홍길순", "1964-10-22", "여성")
    print("================================================")
    selectTableSubject()
    print("================================================")
    selectTableSubjectRaw()
    print("================================================")
    selectTableTestID()
    print("================================================")
    selectTableTestIDRaw()

    # selectTableSubjectKeywords(text_name="김종우")
    # selectTableSubjectKeywords(text_birth_date="821034")
    # selectDataFromTable("Lemon")

    # insertTableTestID("최종우", "1958-11-09", "남성", strnow, 10,\
    #         "비오나", "장미미", "비오나", "장미미", "장미미", "장미미", \
    #         "비오나", "장미미", "비오나", "장미미", "장미미", "장미미", \
    #         "비오나", "장미미", "장미미", "장미미", "비오나", "장미미", \
    #         "비오나", "장미미", "장미미", "비오나", "장미미", "장미미")
    # selectTableTestIDKeywords("최종우", "1958-11-09", "남성")