## Introduction to Machine Learning (ML)
- Machine learning이란... 우리가 "정확하게 프로그래밍하지 않고도" 배우는 능력을 얻는 것.
- *task T*에 대해 *performance meausre P*를 고려하여 *experience E*를 바탕으로 학습.

## Categories of ML
1. Supervised learning : 예측에 대한 정답이 주어짐. 지도학습.
 - Classification (predicting a cateogry. 암이 악성인지/양성인지), Regression (predicting a continous value. 암 환자의 생존기간 등)
2. Unsupervised learning : 예측에 대한 정답이 주어지지 않고, 데이터만 준다. 비지도학습.
 - Clustering (비슷한 샘플들끼리의 그룹핑), Dimension reduction (샘플을 표현할 수 있는 요소가 많을 때 dimension을 줄여 일반화하는 것. gene expression 등. 2D로 줄여 시각화), association (데이터 내의 요소들끼리의 관계성 찾기)
4. Reinforcement leraning : Reward가 존재, reward를 많이 받기 위한 방향으로 학습.

## Supervised Learning
- 입력 `X` (input feature)를 출력 `Y` (estimated output. $\hat{y}$로 표현)로 매칭하는 함수 `f`를 찾는 것. 학습되지 않은 샘플이 들어왔을 때 f를 통해서 해당하는 Y를 추정할 수 있도록, 이 함수 f를 찾는 것이 곧 model training.
1. Get data
2. Preprocess data : Impute missing values (결측치를 채워넣기), Normalize data (들쭉날쭉한 것을 맞춰주기), Feature selection, Prepare training/validation/test sets
3. Train a machine learning model 
4. Evaluate the trained model

## Supervised Learning Algorithms - Linear Regression
- 예측하고 싶은 것이 continuous variable일 때 쓰는 알고리즘. 딥러닝 등의 모델의 기본!
  - 알고리즘은 왜 이렇게 다양한 것인가? 모든 문제에 보편적으로 적용할 수 있는 모델이 존재하는 게 아니기 때문. 문제별로 가장 잘 작동하는 model이 다르므로, 어떤 모델이 가장 적합할 지 여러 알고리즘을 시도해보아야 한다!

 <img width="500" alt="Screen Shot 2022-12-13 at 10 54 56 PM" src="https://user-images.githubusercontent.com/47490862/207352301-d1151eb9-9880-45e0-a786-914cb573ebc2.png">

- w, b : parameter. coefficient. weight. hyperparameter는 다른 것이다 (모델을 학습할 때 지정해줘야 하는 값들).
   - w : weight. 기울기, b : bias. y절편. 모델을 통해 학습해야 하는 parameter들!
  
<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207359405-7489b317-ae20-4412-a2ac-e1aaa753c1b1.png">

- Cost function J : 모델이 샘플을 표현하는 함수 f를 얼마나 잘 찾았는가를 측정하기 위해서 정의. 
  - error를 제곱한 것(squared error)을 평균내는 것과 비슷. 목표는 모든 X(i), y(i)에 대해 $\hat{y}$(i)가 실제 y값과 가장 가까워질 수 있는 w,b를 찾는 것이 목표! minimize J!
    - b = 0 일 때, J는 w에 대한 이차함수로 표현됨.
    - b != 0일 때, J는 아래로 볼록한 3차원 그래프로 표현됨.
- J를 찾는 방법? w, b를 랜덤하게 반복하면서 최저의 J가 나올 때까지 반복한다. 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207359868-fea9e09e-7655-4704-8b14-a6bc7a62a508.png">

- **Gradient descent** -> 동산의 꼭대기에 서서 경사가 가파른 방향으로 한걸음씩 가면서 동산의 최저점에 다다르는 것!
- 새로운 w값 = 원래의 w값에서 그 특정 w값 시점에서의 J의 기울기값을 subtract. 
  - 여기서 alpha : 걸음의 보폭! learning rate. 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207360419-3aa6b0cf-ef71-4b20-aada-470753636e46.png">

- if... alpha가 너무 커지면? overshooting. minimum에 가지 못하고, cost가 수렴이 아니라 발산해버림.
- 반대로, alpha가 너무 작으면? gradient descent가 느려서 학습이 너무 오래 걸리게 된다. 또한 local minimum에 걸려서 빠져나가지 못하고 global minimum으로 진행되지를 못함.
- 기울기가 0이 되는 경우 w의 업데이트를 멈춤. local minimum (test한 범위 내에서의 minimum) 
  - 데이터 전체에 걸쳐 존재하는 minimum = global minimum. 찾는 건 불가능.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207366849-1ba2ca8a-c160-4c36-b5f7-ce894235cb40.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207368908-9127cb86-2307-4651-950d-5f5e134fe491.png">

- 처음 학습할 때는 learning rate를 크게 하고, 학습이 진행될수록 rate가 점점 작아지도록 한다!
- Learning rate : **Hyperparameter**. 학습 대상이 아니고, 우리가 지정해주는 model의 특성! 적절하게 지정하는 것이 필요함.
- x축을 반복횟수 (iteration), y축을 min(J)로 step을 움직이는 것에 따른 learning curve를 그렸을 때, 일정 iteration 이후에는 J가 거의 변하지 않고 일정 값으로 수렴한다. 이 때, J가 아주 작은 값 (epsilon)보다 더 작아지게 되면 학습을 중단!
- alpha 값을 3배씩 늘려가보면서, learning curve의 형태가 어떻게 변하는지 보고, 이상적인 convergence를 나타내는 learning rate를 잡아준다!

<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207367040-e88a671b-dd26-4cd2-9430-9cedc3a50e66.png">

- w에 대한 미분값, b에 대한 미분값이 모두 0에 근사하여 cost값이 최소가 될 때까지 계산을 진행한다!

<img width="500" alt="image" src="https://user-images.githubusercontent.com/47490862/207367421-fbf516e4-83c8-4b64-a082-11abe5aeb227.png">

- single feature : feature가 하나. fw,b(x) = wx + b.
- multiple figure : fw,b(x) = w1x1 + w2xw + .... wnxn + b. feature 수가 너무 많아지는 경우, 수식으로 길게 표현하기 부담스럽기 때문에 vector 형태로 표현한다. Multiple linear regression. vector의 내적으로 표현!
- feature를 제곱, 세제곱해야하는 polynomial regression의 경우도 있다. Regression식이 1차함수가 아니라 2차함수, 3차함수가 가장 데이터에 적합할 수 있기 때문에. 이 모든 것을 테스팅하여 적절한 모델을 설정하게 된다!


 

