serialText = {
    'status_open': 'Serial port is opened.',
    'status_close': 'Serial port is not opened.',
    'status_connect': '연결됨', #'Connect',
    'status_disconnect': '연결안됨', #'Disconnect',
    'try_connect': '연결하기', #'Connect',
    'try_disconnect': '연결끊기', #'Disconnect',
}

subjectText = {
    'not_selected': '피검자 선택 후, 진행하시기 바랍니다.',
    'existed': '이미 등록된 사용자입니다.',
    'empty_name': '이름 칸이 비워져 있습니다.'
}

processText = {
    'cleaning': '코를 띄어주세요. 세정 중입니다.',
    'question_number': '문항',
    'progress_scent': '발향 중입니다.',
    'progress_scent_1': '1번 향기 발향 중입니다.',
    'progress_scent_2': '2번 향기 발향 중입니다.',
    'progress_scent_3': '2번 향기 발향 중입니다.',
    'question_threshold': '향이 느껴진 번호를 선택하세요.',
    'try_scent_threshold': '검사용 향을 확인해보시기 바랍니다.',\
    'question_discrimination': '다른 향기가 느껴진 번호를 한 개만 선택하세요.',
    'question_identification': '어떤 향이 느껴졌는지 아래 보기에서 선택하세요.',
    'question_train_st': '[자가 평가]\n향이 느껴진 강도를 0 ~ 10 중에서 평가하세요.',
}
# dsText.processText['question_number']

resultText = {
    'index': '문항',
    'scent_no1': '향1번호',
    'scent_no2': '향2번호',
    'scent_no3': '향3번호',
    'answer': '정답',
    'response': '선택',
    'is_correct': '응답여부',
    'index_correct': '정답',
    'index_incorrect': '오답답',

    'results_data_path': 'data',
    'results_data_raw_path': 'data_raw',
    'results_save': 'data 폴더에 저장되었습니다.',
    'results_save_none': '저장할 데이터가 없습니다.',

    'result_test_threshold_title': '후각 역치검사 결과',
    'result_test_threshold_score': '역치검사 점수',
    'result_test_threshold_seq': '회차',
    'result_test_threshold_level': '역치',
    'result_test_threshold_density': '향 농도도',
    'result_test_threshold_time': '시간',
    'result_test_threshold_point': '점수',
    'result_test_threshold_range': '12',
    
    'result_test_discrimination_title': '후각 식별검사 결과',
    'result_test_discrimination_score': '식별검사 점수',
    'result_test_discrimination_seq': '회차',
    'result_test_discrimination_correct': '정답',
    'result_test_discrimination_incorrect': '오답',
    'result_test_discrimination_time': '시간',
    'result_test_discrimination_point': '점수',
    'result_test_discrimination_range': '12',
    
    'result_test_identification_title': '후각 인지검사 결과',
    'result_test_identification_score': '인지검사 점수',
    'result_test_identification_seq': '회차',
    'result_test_identification_correct': '정답',
    'result_test_identification_incorrect': '오답',
    'result_test_identification_time': '시간',
    'result_test_identification_point': '점수',
    'result_test_identification_range': '12',
}
# dsText.resultText['result_test_identification_title']

reportText = {
    'report_data_path': 'data',
    'report_data_temp_path': 'data_temp',
    
    'report_sheet': 'DigitalOlfactoryTestReport',
    'report_sheet_threshold': 'Threshold',
    'report_sheet_discrimination': 'Discrimination',
    'report_sheet_identification': 'Identification',

    'report_title': '디지털 후각 검사 결과지 (Digital Olfactory Test Report)',
    'report_reg_num': '등록번호',
    'report_date': '검사일자',
    'report_name': '이름',
    'report_gender': '성별',
    'report_birth_date': '생년월일',
    # 'report_both_nostrils': '양측(   )',
    # 'report_right_nostril': '우측(   )',
    # 'report_left_nostril': '좌측(   )',
    'report_ammonia': 'Ammonia Response',
    'report_total_score': '종합 점수',
    'report_nomosmia': 'Nomosmia',
    'report_hyposmia': 'Hyposmia',
    'report_anosmia': 'Anosmia',
}
# dsText.reportText['report_sheet_threshold']

reviewText = {
    'review_test_title': '평가 의견',
    'review_test_score': '만족도/불편도 점수',
    'review_test_range': '12',
}

pwText = {
    'pwDefault': "!digitalscent1234",
    'pwChange': "비밀번호가 변경되었습니다.",
    'pwRequirement': "비밀번호: 영문/숫자/특수문자 조합 8자~20자",
    'pwCheckError': "변경된 비밀번호가 일치하지 않습니다.",
    'pwOldError': "기존 비밀번호가 맞지 않습니다."
}

pwErrorText = [
    "비밀번호가 맞지 않습니다.\n다시 확인해주십시오.",
    "비밀번호 1회 오류\n(5회 오류시 로그인 불가)",
    "비밀번호 2회 오류\n(5회 오류시 로그인 불가)",
    "비밀번호 3회 오류\n(5회 오류시 로그인 불가)",
    "비밀번호 4회 오류\n(5회 오류시 로그인 불가)",
    "비밀번호 5회 오류\n(관리자 문의 요망)"
]
# dsText.reviewText['review_test_range']

errorText = {
    'disconnect': '발향 장치 연결을 확인해주십시오',
    'scent_fail': '발향 실패하였습니다.',
    'clean_fail': '세정 실패하였습니다.',
    'setting_value': '설정값을 확인해주세요.',
    'file_save_fail': '저장 실패하였습니다.',
    'password_fail': '비밀번호 5번 이상 맞지 않아서 재설정이 필요합니다.',
    'db_select_subject_fail': '사용자 정보 조회 실패하였습니다.',
    'db_select_test_id_fail': '검사 정보 조회 실패하였습니다.'
}

# 주관식 처리 필요
# 감각 훈련 처리 필요
# saveData 년, 월, 일 처리
