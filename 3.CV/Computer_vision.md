# Computer Vision

## 6. 특징

#### SIFT 기술자

* 불변성

  * 스케일 불변
    찾은 점에 patch를 씌운다. patch의 메인 방향을 구한다. 

  * 회전 불변 달성(Rotation Robust)

    ## gradient방향의 수직의 되도록 patch를 씌운다. 특징을 뽑아서 나중에 비교한다. 

    전체에 대한 메인 그래디언트 방향을 찾아서 수직이도론 윈도우 패치를 뗀다
    (ex) 건물이 조금 삐뚤어져 있어도 메인 gradient방향은 안 바뀌니깐 robust한 feature를 찾을 수 있다.
    grid cell 나눴을 때 방향(8방향)에 대한 히스토그램으로 비교한다. 

  * 

Multiscaler(최소 윈도 크기 scale factors)



* 영상 피라미드마다 피처를 뽑음
* 현재의 도그맵에서 이전 현재 이후 다른 곳을 뽑아 비교한 피처로 뽑은



### 민시프트

* 윈도우 크기에 따라 중심점 찾는게 달라진다



## 매칭

### 거리 척도

#### 유클리디안 거리

#### 마할노비스 거리

* 미리 학습된 데이터의 분포를 알아야됨
* full search를 할 수도 있지만, 이진트리 검색



## 기계학습

#### 부트스트랩

1. 뽑고 다시 넣고 해서 여러 개의 분류기를 만든다. 얘들을 합친다 그게 앙상블
   ex) 여러 개의 의사가 환자라르 진단해서 무슨 병인지 맞춘다.(의사가 분류기)
   * svm :무거움
   * adaaboost : 앙상블 협동 분류기다
   * random forest 



#### Boosting

1. 연관성을 갖고 이전 분류기의 결과르라 다시 분류하는 시스템



#### 유사 하르 특징







#### 퍼셉트론

* 뉴럴넷 
* 선형 분리 불가능
  직선을 여러개 둬서 분류를 잘해보자



### Fully Network

1. Network를 첨에 지나서 target이랑 비교해봐서 error를 확인
2. 출력이 이상하게 나오면 답이랑 비교.
3. error크기 만큼 back해서 w값을 조정한다. (iteration하면서)
4. l2 loss 정답가 출력값의 제곱







## Shallow Net VS.Deep Neural Net







# Day2

non-maximum suppression & thresholding

edge 방향성 히스토그램 특징추출 

#### HOG

* 전체 영상에서 각각의 방향값들을 구해놓은ㄴ다. (detection)



Feature map에서 가능성 있는 patch를 확인



딥러닝 초기에는 패치를 떼서 지그재그로 오브젝트인지 확인 

non-maximum suppression : maximum이 아니면 없애버려라

이미지 방향 히스토그램 특징으로 삶아서 오브젝트 디텍트











