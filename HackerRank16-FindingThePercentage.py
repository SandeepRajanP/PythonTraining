if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    avg_student_marks={}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
      	avg_student_marks[name]=sum(scores)/3
    query_name = raw_input()
    print '%.2f' % avg_student_marks[query_name]
