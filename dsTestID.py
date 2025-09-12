import dsText
import random
import copy

id_time_count = 0

id_test_index = 0 # 인지검사 현재 번호
id_temp_response = ""

# 인지검사 결과 데이터
id_results_title = ['문항', '정답', '선택', '정답여부', '응답(주관식)', '정답여부(주관식)']
# id_results_title = ['Question', 'Correct answer', 'Your selection', 'O/X', '응답(주관식)', '정답여부(주관식)']
id_results = []

I_score = 0


# 인지검사 문항 데이터


id_test_data = [
    {'choice1': '땅콩','choice2': '케챱','choice3': '장미','choice4': '양파','answer': '장미','scent_no': 1,'outlet_no': 1,
     'choice5':'비누','choice6':'레몬','choice7':'재/연기','choice8':'국수','choice9':'바나나','choice10':'소나무'},

    {'choice1': '마늘','choice2': '초콜릿','choice3': '오이','choice4': '레몬','answer': '초콜릿','scent_no': 2,'outlet_no': 1,
     'choice5':'사과','choice6':'계피','choice7':'계란','choice8':'버섯','choice9':'홍삼','choice10':'복숭아'},

    {'choice1': '생강','choice2': '솜사탕','choice3': '사과','choice4': '당근','answer': '생강','scent_no': 3,'outlet_no': 1,
     'choice5':'녹차','choice6':'양파','choice7':'옥수수','choice8':'장미','choice9':'국수','choice10':'가죽'},

    {'choice1': '빵','choice2': '겨자','choice3': '오징어','choice4': '마늘','answer': '마늘','scent_no': 4,'outlet_no': 1,
     'choice5':'키위','choice6':'박하','choice7':'바나나','choice8':'생강','choice9':'장미','choice10':'사과'},

    {'choice1': '쌀','choice2': '사과','choice3': '소나무','choice4': '고구마','answer': '소나무','scent_no': 5,'outlet_no': 1,
     'choice5':'겨자','choice6':'딸기','choice7':'계피','choice8':'홍삼','choice9':'멜론','choice10':'계란'},

    {'choice1': '생선','choice2': '아기 분','choice3': '카레','choice4': '키위','answer': '아기 분','scent_no': 6,'outlet_no': 1,
     'choice5':'버섯','choice6':'레몬','choice7':'양파','choice8':'사과','choice9':'국수','choice10':'장미'},

    {'choice1': '녹차','choice2': '마늘','choice3': '간장','choice4': '쇠','answer': '녹차','scent_no': 7,'outlet_no': 1,
     'choice5':'멜론','choice6':'계란','choice7':'국수','choice8':'솜사탕','choice9':'양파','choice10':'복숭아'},

    {'choice1': '후추','choice2': '딸기','choice3': '계란','choice4': '홍삼','answer': '홍삼','scent_no': 8,'outlet_no': 1,
     'choice5':'사과','choice6':'쇠','choice7':'버섯','choice8':'소나무','choice9':'레몬','choice10':'장미'},

    {'choice1': '나무','choice2': '가죽','choice3': '계피','choice4': '김치','answer': '계피','scent_no': 9,'outlet_no': 1,
     'choice5':'박하','choice6':'국수','choice7':'멜론','choice8':'재/연기','choice9':'겨자','choice10':'키위'},

    {'choice1': '후추','choice2': '옥수수','choice3': '바나나','choice4': '잔디','answer': '후추','scent_no': 10,'outlet_no': 1,
     'choice5':'장미','choice6':'겨자','choice7':'복숭아','choice8':'홍삼','choice9':'사과','choice10':'멜론'},

    {'choice1': '꿀','choice2': '버섯','choice3': '박하','choice4': '담배','answer': '박하','scent_no': 11,'outlet_no': 1,
     'choice5':'레몬','choice6':'국수','choice7':'장미','choice8':'사과','choice9':'김치','choice10':'초콜릿'},

    {'choice1': '청포도','choice2': '비누','choice3': '국수','choice4': '고무','answer': '비누','scent_no': 12,'outlet_no': 1,
     'choice5':'사과','choice6':'쇠','choice7':'홍삼','choice8':'계피','choice9':'장미','choice10':'땅콩'}
]

id_test_data2 = [{'choice1': '땅콩',
                 'choice2': '케챱',
                 'choice3': '장미',
                 'choice4': '양파',
                 'answer': '장미',
                 'scent_no': 1,
                 'outlet_no': 1},
                
                {'choice1': '마늘',
                 'choice2': '초콜릿',
                 'choice3': '오이',
                 'choice4': '레몬',
                 'answer': '초콜릿',
                 'scent_no': 2,
                 'outlet_no': 1},

                {'choice1': '생강',
                 'choice2': '솜사탕',
                 'choice3': '사과',
                 'choice4': '당근',
                 'answer': '생강',
                 'scent_no': 3,
                 'outlet_no': 1},

                {'choice1': '빵',
                 'choice2': '겨자',
                 'choice3': '오징어',
                 'choice4': '마늘',
                 'answer': '마늘',
                 'scent_no': 4,
                 'outlet_no': 1},

                {'choice1': '쌀',
                 'choice2': '사과',
                 'choice3': '소나무',
                 'choice4': '고구마',
                 'answer': '소나무',
                 'scent_no': 5,
                 'outlet_no': 1},

                {'choice1': '생선',
                 'choice2': '아기 분',
                 'choice3': '카레',
                 'choice4': '키위',
                 'answer': '아기 분',
                 'scent_no': 6,
                 'outlet_no': 1},

                {'choice1': '녹차',
                 'choice2': '마늘',
                 'choice3': '간장',
                 'choice4': '쇠',
                 'answer': '녹차',
                 'scent_no': 7,
                 'outlet_no': 1},

                {'choice1': '후추',
                 'choice2': '딸기',
                 'choice3': '계란',
                 'choice4': '홍삼',
                 'answer': '홍삼',
                 'scent_no': 8,
                 'outlet_no': 1},
                 
                {'choice1': '나무',
                 'choice2': '가죽',
                 'choice3': '복숭아',
                 'choice4': '김치',
                 'answer': '복숭아',
                 'scent_no': 9,
                 'outlet_no': 1},
                 
                {'choice1': '재/연기',
                 'choice2': '옥수수',
                 'choice3': '바나나',
                 'choice4': '잔디',
                 'answer': '재/연기',
                 'scent_no': 10,
                 'outlet_no': 1},

                {'choice1': '꿀',
                 'choice2': '버섯',
                 'choice3': '박하',
                 'choice4': '담배',
                 'answer': '박하',
                 'scent_no': 11,
                 'outlet_no': 1},

                {'choice1': '청포도',
                 'choice2': '비누',
                 'choice3': '국수',
                 'choice4': '고무',
                 'answer': '비누',
                 'scent_no': 12,
                 'outlet_no': 1}
                 ]

# 튜닝 가능: 3지선다 & 8문항
NUM_SELECTED_OPTIONS = 3
NUM_QUESTIONS = 8

# 12문항 원본 백업 버퍼
try:
    id_test_data_full
except NameError:
    id_test_data_full = None

def _collect_choices(q, max_n=20):
    """문항 딕셔너리에서 choice1..choiceN을 모두 수집 (중복 제거)."""
    seen = set()
    choices = []
    for i in range(1, max_n+1):
        k = f"choice{i}"
        if k in q and q[k] and q[k] not in seen:
            seen.add(q[k])
            choices.append(q[k])
    return choices

def rebuild_to_3choice_and_sample_8():
    global id_test_data, id_test_data_full

    # 최초 1회 원본 보존(=지금의 choice10까지 확장된 테이블)
    if id_test_data_full is None:
        id_test_data_full = copy.deepcopy(id_test_data)

    rebuilt = []
    # 전체 정답 풀 (오답 보충용)
    global_answers = [q['answer'] for q in id_test_data_full if 'answer' in q]

    for q in id_test_data_full:
        ans = q['answer']
        pool = _collect_choices(q, max_n=20)

        # 정답이 빠져있으면 강제 포함
        if ans not in pool:
            pool = [ans] + pool

        wrongs = [c for c in pool if c != ans]
        need = (NUM_SELECTED_OPTIONS - 1)

        # 오답 후보가 부족하면 전체 정답 풀에서 보충(자기 정답 제외)
        if len(wrongs) < need:
            supl = [x for x in global_answers if x != ans and x not in wrongs]
            while len(wrongs) < need and supl:
                take = random.choice(supl)
                supl.remove(take)
                wrongs.append(take)

        # 최종 보기 3개(정답 1 + 오답 2)
        final_opts = [ans] + random.sample(wrongs, need)
        random.shuffle(final_opts)

        new_q = {
            'scent_no': q.get('scent_no', None),
            'outlet_no': q.get('outlet_no', 1),
            'answer': ans,
            'choice1': final_opts[0],
            'choice2': final_opts[1],
            'choice3': final_opts[2],
        }
        rebuilt.append(new_q)

    # 문항 셔플 → 앞의 8문항만 사용
    random.shuffle(rebuilt)
    id_test_data = rebuilt[:NUM_QUESTIONS]