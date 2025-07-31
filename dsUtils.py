import re

def hoursFromCount(time_count):
    return time_count/3600
    
def minutesFromCount(time_count):
    return (time_count%3600)/60
    
def secondsFromCount(time_count):
    return time_count%60
    
def hmsFormFromCounts(time_count):
    if hoursFromCount(time_count) > 1:
        form = "%02d : %02d : %02d" \
            % (hoursFromCount(time_count), 
               minutesFromCount(time_count),
               secondsFromCount(time_count))
    else:
        form = "%02d : %02d" \
            % (minutesFromCount(time_count),
               secondsFromCount(time_count))
    return form

def isCorrectToOX(is_correct):
    if is_correct == 1:
        return "O"
    elif is_correct == '정답여부':
        return "O/X"
    else:
        return "X"

def average(list):
    if len(list) > 0:
        return sum(list) / len(list)
    else:
        return 0

def is_valid_password(password):
  """
  8자리 이상 영문, 숫자, 특수문자 조합 비밀번호인지 확인하는 함수
  """
  pattern = r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*\W).{8,}$"
  match = re.match(pattern, password)
  return bool(match)
