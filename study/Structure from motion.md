# Structure from motion
## 스터디 목표 
- COLMAP, MeshLab 등 여러 오픈소스 툴을 사용하여 스마트폰으로 촬영한 사진을 3d로 변환해본다. 
- 2d -> 3d 이미지 변환과 관련된 여러 원리(SfM 등)를 이해한다.
## 관련 개념 
- 어떤 변환(A)의 결과로 좌표 b를 알 때, 원래 좌표 x를 알아내는 방법
- 참고 자료: https://www.youtube.com/watch?v=JlOzyyhk1v0&list=PLWhN6ilQm9EU8-FJVrqzZ2OdSaB6xFAJ2&index=2 
### Structure from motion 
- 결과물(2d 이미지)를 통해 원인(3d 물체 + 카메라의 움직임)을 계산해내는 과정 및 방법을 일컫는다.  
### 삼각 측량
### SFM Observation Matrix (관측 행렬)
- 특정 시점(frame)에서 각 점들의 2d 좌표상의 위치(point)의 집합
### Rank of Observation Matrix (관측 행렬의 Rank) 


## Tools
- **COLMAP**: 2d 이미지를 3d 점군 데이터로 변환하는 편집기
  - input: 여러장의 2d 이미지
  - output: 3d 점군 데이터 (`.ply`)
    - 점군 데이터(Point clous) 란?: 3차원 공간상에 흩뿌려진 점들의 집합
  - 관련 개념: SfM(Structure from Motion), MVS(Multi-VEiw Stereo)
- **MeshLab**: 점군 데이터를 메쉬로 변환하고 텍스처링을 입히는 편집기
  - input: 3d 점군 데이터
  - output: 메쉬 (`.obj`, `.stl`)
    - 메쉬(Mesh)란?: 점과 점을 이은 면들의 집합
  - 관련 개념: Surface Reconstruction(e.g. Poisson Reconstruction), Cleaning, Simplification
