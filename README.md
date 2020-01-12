# sig-health-slackbot
팀원을 건강하게 만드는 슬랙봇.


## Features

- [x] 메타 기능
    - [x] `#sig-헬스` 채널을 등록할 수 있다.
- [x] 운동 인정 기능
    - [x] `인정 이모지` 를 등록할 수 있다.
    - [x] `최소 인정 이모지 횟수` 를 등록할 수 있다.
    - [x] `최소 인정 이모지 횟수` 를 넘는 사람이 `인정 이모지` 를 찍으면 유저의 그 날의 운동이 인정된다.
    - [x] `주별 운동 횟수에 따른 응원 멘트` 를 정할 수 있고, 운동이 인정되면 봇이 응원해준다.
- [ ] 정회원 기능
    - [x] 등록
        - [x] `정회원 주 별 최소 운동 횟수` 를 정할 수 있다.
        - [x] 일주일에 정해진 횟수를 채우면 특정 회원이 `#sig-헬스` 정회원으로 등록된다.
        - [x] `#sig-헬스` 정회원으로 등록되면 봇이 축하해준다.
    - [x] 리액션 이모지
        - [x] `정회원 리액션 이모지` 를 등록할 수 있다.
        - [x] 정회원이 말을 할 때마다 별건 없고 귀여운 이모지가 달린다.
    - [ ] 탈퇴
        - [ ] 선택한 주의 정회원 체크 후 탈퇴하는 management command가 있다.
            - [ ] 선택한 주가 지나지 않으면 돌릴 수 없다.
            - [ ] 선택한 주의 운동 횟수가 `정회원 주 별 최소 운동 횟수` 보다 작으면 정회원에서 탈락한다.
                - [ ] `탈락 안타까움 멘트` 가 채널로 발송된다.
            - [ ] 매 주 월요일마다 배치가 돈다. 
        - [ ] 정회원 탈락시 `정회원 리액션 이모지` 가 더이상 달리지 않는다.
