#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
INPUT = open(sys.argv[1])

class Player():
    name = None
    shot_percentage = None
    height = None
    draft = None
    time_played = 0

T = int(INPUT.readline().strip())

for t in range(1, T + 1):
    N, M, P = [int(x) for x in INPUT.readline().strip().split(' ')]
    PLAYERS = []
    for _ in range(N):
        player = Player()
        player.name, s, h = INPUT.readline().strip().split(' ')
        player.shot_percentage, player.height = int(s), int(h)
        PLAYERS.append(player)

    PLAYERS.sort(reverse=True, key=lambda p: (p.shot_percentage, p.height))
    for n, p in enumerate(PLAYERS):
        p.draft = n + 1

    TEAM_A = [p for p in PLAYERS if p.draft % 2 != 0]
    TEAM_B = [p for p in PLAYERS if p.draft % 2 == 0]

    PLAYING_A = TEAM_A[:P]
    PLAYING_B = TEAM_B[:P]

    for _ in range(M):
        for TEAM, PLAYING in ((TEAM_A, PLAYING_A), (TEAM_B, PLAYING_B)):
            if len(TEAM) == len(PLAYING): continue

            for p in PLAYING: p.time_played += 1

            BENCH = [p for p in TEAM if p not in PLAYING]

            leaving = sorted(PLAYING, key=lambda p: (p.time_played, p.draft))[-1]
            entering = sorted(BENCH, key=lambda p: (p.time_played, p.draft))[0]

            PLAYING.remove(leaving)
            PLAYING.append(entering)

            BENCH.remove(entering)
            BENCH.append(leaving)

    print('Case #%i: ' % t + ' '.join(sorted(p.name for p in PLAYING_A + PLAYING_B)))
