def solution(routes):
    
    
    camera_count = 0
    
    
    while routes:
        not_scanned = []
        
        
        # 차가 빠져나갈 때를 기준으로 생각해보기
        cam_at_exit = min(car[1] for car in routes)
        camera_count += 1
        
        
        for car in routes:
            # print('looking at...', car)
            # 차가 고속도로에 진입한 시점이 단속카메라 위치 이후일 때
            # # 단속용 카메라를 지나지 않았다!
            if car[0] > cam_at_exit:
                not_scanned.append(car)
            # if car[0] <= cam_at_exit:
            #     routes.remove(car)
            #     print('updated routes', routes)
            
        # 단속용 카메라를 지나지 않은 차들만 필터링
        routes = not_scanned
    
    
    return camera_count


# def solution(routes):
    
    
#     camera_count = 0
    
    
#     while routes:
#         not_scanned = []
        
        
#         # 차가 들어왔을 때를 기준으로 생각해보기
#         cam_at_start = max(car[0] for car in routes)
#         camera_count += 1
        
        
#         for car in routes:
#             # 차가 고속도로에서 진출한 시점이 단속카메라 위치 이전일 때
#             # 단속용 카메라를 지나지 않았다!
#             if car[1] < cam_at_start:
#                 not_scanned.append(car)
            
        
#         # 단속용 카메라를 지나지 않은 차들만 필터링
#         routes = not_scanned
    
    
#     return camera_count