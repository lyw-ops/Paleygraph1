# Paley 主脑交接：第36轮完成，按用户要求暂停

更新时间：2026-11-18，Asia/Shanghai。

用户最新指令是：“这一轮跑完先暂停，我准备换对话框了，帮我生成作为大脑的提示词。”
第36轮已完成验收，两个研究会话及独立审查均已结束。
**没有创建第37轮，也没有需要继续等待的已知运行任务。**
本对话将在交接文件完成后把旧 goal 置为 paused。新对话只有在用户接手提示词后才恢复推进。

## 1. 不得缩小的目标

证明或反驳 ETH Randomstrasse101 Problem 26：
对所有素数 $p\equiv1\pmod4$，令 $Q=\mathbb F_p^{\times2}$，
$H_p$ 是 Paley 图在 $Q$ 上的诱导图，$n=(p-1)/2$，

$$\vartheta(\overline{H_p})/\sqrt n\longrightarrow1.$$

这里是 **ordinary Lovász theta**，不是强化 theta、整个 Paley 图的
clique 猜想、有限素数上的零误差等式，也不是仅 $p\equiv1\pmod8$ 的子序列。
**目前未解。** 已证若干辅助定理、条件完成路线和严格有限证书，不能冒称主目标完成。

官方题目：https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/

## 2. 工作区和工具

- 工作区：/Users/lyuyuwei/Documents/ChatGPT/Paley
- origin：https://github.com/lyw-ops/1-Localization-of-the-Paley-Graph1-Localization-of-the-Paley-Graph.git
- 本地 git ls-files 为零：研究文件目前全部未跟踪；第36轮没有 commit/push。
  远端已配置，但本轮未核对远端内容。不要用重新 clone 或 checkout 覆盖当前本地研究。
- Python：.venv/bin/python；运行脚本用 -B。已装 numpy、scipy、python-flint；
  sympy 未安装。大型计算通常设 OPENBLAS_NUM_THREADS=1、VECLIB_MAXIMUM_THREADS=1。
- 仓库内未发现 AGENTS.md；接手者仍应核对当前环境和指令。
- 数学证明是普通书面证明和独立审计；没有 Lean kernel 验证。
- 用户授权使用 ChatGPT、Codex、多研究会话、Astra、Claude Fable、ChatGPT API。
  最近两轮使用了实际 Codex Astra 会话；第36轮没有调用 API 或 Claude。
  不得把“可以用”写成“已经调用”，也不要输出或记录密钥。
- harness / VibeMath / Conjecture Search / OpenTorus 等既有比较在
  research/ledger.md 的 Tools and working method。避免重做已完成的工具调查。
  OpenTorus 的 Paley clique campaign 与本题目标不同。

推荐首先读：

1. research/phase-endpoint-36-acceptance.json
2. research/ledger.md 最后的第35、36轮及顶部最新路线表
3. research/averaged-mark-35.md
4. research/parallel-cold-complex-36.md
5. research/parallel-audit-36.md
6. research/astra-averaged-positive-36.md
7. research/endpoint-stress-36.md

不要一次读完整个历史台账：很多行很长。按当前问题检索和分段阅读。

## 3. 核心记号

$q=2n+1$，$K=F\operatorname{diag}(s)F^{-1}$ 是实际实偶 Paley 算子，
$K^2=I-J$，$K1=0$，$K_{ii}=-1/n$，$|K_{ij}|\le\sqrt q/n$。
$P_\sigma=(I-J+\sigma K)/2$。

权重 $w_0=1$，$w_i=c=\tau/n$（其余位置），
$W=1+(n-1)c$，$a=\sqrt{W/n}$。
实际正平稳对为 $A=a1+x$、$B=a1+y$，
$x\in V_+$、$y\in V_-$，$AB=w$，两者均值为 $a$，
$A_0B_0=1$。标记量 $m=\log A_0$。

$\theta_+=\vartheta(\overline H)$，$\theta_-=\vartheta(H)$，
$\theta_+\theta_-=n$。
任意正/非负、均值一的对应扇区谱 $p,q$ 给
$p_0\le\theta_+\le n/q_0$。

平方阶 $q=r^2$ 是必须保留的负对照：
$\theta_+=r-1$，$\theta_-=(r+1)/2$，归一化目标极限是 $\sqrt2$，
不是一。很多固定深度算术输入同时适用于素数和平方阶。

## 4. 当前优先路线：平均提案的正性补全

精确零起 Picard 轨道：

$$
v_0=0,\quad v_{t+1}=K\phi_t,\quad
\phi_t=\sqrt{v_t^2+4w},\quad
\mu_t=\mathbb E\phi_t/2,\quad E_t=\|v_t\|_2^2.
$$

第35轮已经验收：

$$E_{t+1}-E_t=4W-4n\mu_t^2.$$

取 $M_T=T^{-1}\sum_{t=1}^T\mu_t$，
$A_{\sigma,t}=(\phi_t+\sigma v_t)/2$，

$$
X_{\sigma,T}=M_T1+T^{-1}\sum_{t=1}^T P_\sigma A_{\sigma,t},
\quad z_{\sigma,T}=X_{\sigma,T}/M_T.
$$

精确均值预算：

$$
nM_T^2\le B_{n,T}
=W+\frac{(1-\sqrt c)^2(1-1/n)}T
\longrightarrow1+\tau+1/T.
$$

继承的固定深度 marked cancellation 给
$X_{+,T}(0),X_{-,T}(0)\to1$。
若能保均值、扇区和标记把两行补成非负，就直接夹逼 theta。
**这条构造路线不需要另证 conic $D/\kappa$、UI、HR 或原来的逆矩比较。**
但素数一致的适当深度补全仍未证明。

增长深度需要真正的标记条件，例如
$T_n^{-1}\sum_{t=0}^{T_n+1}|v_t(0)|^2\to0$；
不能把 fixed-depth theorem 擅自延长。
原有已证的同时算术窗口很短；具体看 parallel-depth-window-30.md。

第36轮的新统一基线：

- Astra：不修补的精确平均在显式 $O_\tau(n^{3/2})$ 深度后严格为正。
- 独立审查：利用实际 endpoint deficit 和一次 pinned reflection，
  给出 $O_\tau(n^{5/4})$ 的正性补全；保留原均值、扇区和 mark。
  安全常数很大，只改善固定 $\tau$ 下的渐近指数，不保证现列有限素数的数值阈值更小。
- 两者都适用于平方阶，因此不可能自动给出所需标记极限。
  **正性可证的多项式深度与 marked arithmetic 可证窗口尚未衔接。**
- 递减权重的绝对 endpoint 估计中，均匀权重是最优；
  这是该估计的限制，不是所有加权/有符号构造不可能。

## 5. 当前另一主线：共同冷域足够，复增长已自动解决

research/parallel-cold-complex-36.md 的新结论已由主线和独立审查接受：

只要实际标记标量在某连通右半平面域内单值全纯延拓，

$$|\Im m_q(\tau)|\le \tfrac12|\arg W(\tau)|<\pi/4.$$

证明从共轭 stationary pairing 得到 sector inequality，
再用 saturated physical irreducible algebraic curve 的 generic lift，
所以**不需要整行谱也单值延拓**。零点/相位连通性已经检查。
strip Schwarz 估计使共同域上的紧子域增长自动一致有界。

因此复分析路线现在只需证明：
对每个所需冷点 $a_j\downarrow0$，实际素数标记 germ 有共同的
右半平面冷–热全纯域。**不再需要另立 subpolynomial growth 或 phase 假设。**
这个 prime common domain 仍完全未证。

已有热域：$\Re\tau>0,\ 1024<|\tau|<n$，
完整互易谱全纯逐坐标非零，$|m_q|\le4/\sqrt n$。
冷端全 Hessian isotropic 球证书宽度为 $\Theta_a(n^{-1/2})$，
只限制该方法，不能声称实际奇点离实轴这么近。

平方族的新严格障碍：
当 $q=2n+1$ 是奇平方 prime power 且 $n>e^{100000}$，
实际标记代数分支有可达的真正 ramification point，
$\Re\tau>1/16,\ |\tau|\le1024$。
由实际热 Taylor germ 的首个奇点追踪，local winding 排除了普通零极点。
没有算出某个可管理有限域的具体位置。

有限场旧结论仍保留：$p=13,17$ 和 $q=25$ 的相应右半平面延拓已证。
小平方例子不与大平方族分歧定理冲突。
第35轮对 $m,A_0,u_0$ 的 Pick/Stieltjes 反证针对整个上半平面，
不能误用来反驳右半平面 holomorphy。

## 6. 本轮有限证书与严格边界

research/astra-averaged-positive-36-replay224.jsonl：
四个 saved-input 案例，精确有理 Fourier 输入起算。

- $9413,1000033$ 的 $T=128$ 一次修补严格为正。
  百万素数的 plus 最小正裕量 $>4.737707156\times10^{-5}$。
  $0.001$ 是 reserve 参数，不是本路线输出必须达到的 floor。
- 两个素数的 $T=64$ saved-input 修补严格负。
- rounded 输入不自动继承精确 Picard mean budget；有限 theta 界直接用其精确 Fourier marks。

主线更大素数压力测试：

- endpoint-stress-36.py 用 endpoint identity 将平均生成降为每步一次 $K$ FFT；
  小场与 direct projection 比较通过。
- $p=7340033,T=128,\tau=.05,\kappa=.001$ 的
  endpoint-stress-36-p7340033-t128-input.json.gz 约44MB。
- Arb128 严格证明 minus coordinate 2136334
  $<-.0002282579562724539$；plus 行仍正。
- 第二次完整 interval replay 字节一致。
- **只反驳该精确保存的 Fourier-rounded trial。**
  未对大浮点前缀做 exact-orbit shadowing，不得称其严格反驳 unrounded Picard，
  不得推出 eventual uniform failure、其他 completion 不存在或主猜想为假。

此前平方 saved minus mark $267.6044\ldots>195$ 是另一种更强障碍：
所有保该 mark、mean-one、minus-sector 的非负补全都不可能。
不要把这个平方论证挪到新的素数负例。

## 7. 验收、复算与文件分工

最新权威验收：research/phase-endpoint-36-acceptance.json。
本轮44条核心记录：

- Astra224 finite trials：4；
- weighted endpoint / horizon audit：12；
- cold-complex exact / Arb：8；
- 独立 endpoint audit：19（含明确标注的浮点实现检查）；
- 主线大素数负证书：1。

所有核心记录独立重放；五个新的 exact saved inputs 保留哈希。
普通证明、interval certificates、floating diagnostics、proposal provenance 分开记录。
重复/探索记录没有冒充额外定理。

常用命令：

    .venv/bin/python -B research/parallel-cold-complex-36.py
    .venv/bin/python -B research/parallel-audit-36.py
    .venv/bin/python -B research/astra-averaged-positive-36.py --endpoint-audit --precision 192
    .venv/bin/python -B research/astra-averaged-positive-36.py --precision 224 --replay INPUT_PATH

大负例用 --precision 128 回放即可。先读 acceptance 内 exact_input 与哈希，
不要因 /tmp replay 消失而把 canonical input 误判丢失；脚本和保存输入可以重新生成验证。

还有一条**尚未验收的末尾探索**：

- research/marked-pick-jets-36.py
- research/marked-pick-jets-36-probe.jsonl

它在等权点用 rational cyclic-convolution recurrence 生成实际 root Taylor jets，
试探 phase theorem 对
$-\log u_{\sigma,0}(n\sqrt{1+z})$ 的 transformed Pick 必要条件。
401 与 $19^2$、两侧、16阶 Hankel leading minors 都正。
这四条 exact probe 及其理论解释未独立审查，**不计入本轮验收**。
有限正 minors 不证明 continuation、无分支点或极限。
若继续这条线，先补独立推导和已知小场 cross-check，别直接将其升级为定理。

## 8. 已结束的会话，不要重启

本轮研究会话：

1. Astra positive completion：
   01a1ecea-3bf2-7e21-aaa2-80ba39fb4a8e，host local，
   latest turn completed，cursor 2e01e8fd-bf73-44a5-9779-8f3d406fac71:6。
2. Astra cold complex：
   01a1ecea-3db5-73f2-94d6-9dd3c5ea61c9，host local，
   latest turn completed，cursor 4a891190-cac0-43a4-8c39-920f81f9dc82:5。
3. 内部 /root/audit_square 已 completed。

桌面显示 notLoaded 不改变已确认的 latestTurn.completed。
research/round-36-dispatch.json 记录派发，验收记录记录完成。
没有第37轮会话，也没有待轮询的已知进程。

## 9. 新主脑的工作方式与下一步

用户要的是“你当大脑”，不是只接收子会话结论。
接手后自己推导数学、选择互补路线、控制实际会话、独立验收并记录比较。
已有授权允许验收后再开多会话；难点可给 Astra 或可用的 Claude Fable。
若重新开始第37轮，应是新指令下的新工作，不是在本次暂停期间自动派发。

建议优先级：

1. 主攻：缩短实际平均提案的正性补全深度，或在真实长深度证明 marked Cesaro
   控制。保持 mean/sector/mark budget，别再把更强的 UI rate 当本路线必需条件。
2. 备线：利用 automatic phase theorem 攻 prime common cold domain，
   或找到能指导共同域问题的实际 scalar ramification 信息。
3. 对数值现象明确区分 rounded-input certificate 与 exact-orbit theorem；
   有限反例既不能反驳 asymptotic 猜想，也不能反驳 eventual algorithm。
4. 不要只积累更多等价条件、无关小 family 反例或更长 prime 列表。
   优先证明真正的素数一致估计；失败也应给具体、可复核且改变下一步的证据。

向用户中文汇报，简明说明新结论、其作用和未解处。进行中约每分钟给有意义更新。
默认自主推进，不重复询问已经授权的工具使用或并行安排。
遇到 observation timeout 继续查同一实际 handle，不因超时或无草稿重启会话。
