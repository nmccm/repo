# PostgreSQL performance 

## postgresql.conf

출처 : http://postgresql.kr/blog/simple_postgresql_conf.html

```linux
listen_addresses = '*'                       # 로컬 호스트 밖에서의 접속 허용
shared_buffers = 3GB                         # 물리 메모리  2/3 ~ 1/4
checkpoint_segments = 128                    # 2GB redo 로그, 9.4 이하에서
max_wal_size = 2GB                           # 2GB redo 로그, 9.5 이상에서
min_wal_size = 2GB                           # 2GB redo 로그, 9.5 이상에서
wal_level = logical                          # 일단 최대 자세하게
archive_mode = on                            # 아카이빙 기능은 켜두고,
archive_command = 'true'                     # 아카이빙을 임시로 사용 안함
log_destination = 'stderr'                   # pg_log 에 로그 남김
logging_collector = on                       # 자체 로그 프로세스 사용
log_line_prefix = '%t %u@%r/%d(%c 또는 %p) ' # 좀 더 자세히
stats_temp_directory = '/run/shm'            # 실시간 통계 정보는 공유 메모리로
effective_cache_size = 4GB                   # 물리 메모리 1/2 , 9.4 이하
```







