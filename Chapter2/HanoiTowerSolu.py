def HanoiTowerMove(num, start, end, to):
    if num == 1:                # 이동할 원반의 수가 1개라면
        print(f"원반1을 {start}에서 {to}로 이동")
    else:
        HanoiTowerMove(num - 1, start, to, end)
        print(f"원반{num}을(를) {start}에서 {to}로 이동")
        HanoiTowerMove(num - 1, end, start, to)


if __name__ == '__main__':
    # 막대A의 원반 3개를 막대B를 경유하여 막대C로 옮기기
    HanoiTowerMove(3, 'A', 'B', 'C')
