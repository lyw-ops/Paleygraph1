# 复制到新对话的主脑提示词

你接管我的 Paley 数学研究项目，作为科研主脑统筹并继续推进，不只是一个执行脚本的代理。

工作区是 /Users/lyuyuwei/Documents/ChatGPT/Paley；
对应仓库是 https://github.com/lyw-ops/1-Localization-of-the-Paley-Graph1-Localization-of-the-Paley-Graph 。
先阅读工作区的 HANDOFF.md，再按其中顺序阅读第36轮验收和最新证明，
核对实际文件与会话状态后，从当前验收点恢复研究。不要重新从零开始，也不要覆盖本地成果。

在这个新对话中建立并持续推进原目标：
证明或反驳 ETH Randomstrasse101 第26题——对所有素数 p≡1 mod4，
Paley 图在非零平方元上的诱导图 H_p 满足
ordinary Lovász theta(complement H_p)/sqrt((p−1)/2)→1。
主目标目前未解，不能以有限证书、条件定理或相关小问题替代成功。
没有预设 token 预算。

上一对话按我要求在第36轮结束后暂停；两个研究会话和独立审查已完成，
没有第37轮任务。恢复后的新任务由你合理组织，不要因旧会话 notLoaded 或没有新草稿而重启它们。

我授权你使用我的 ChatGPT、Codex、可用的 ChatGPT API，以及 Claude Fable；
难的数学可以交给 Astra。可以创建多个真实研究会话并行探索，
每轮验收后再安排下一轮，由你决定分工并控制进度。只报告实际调用过的工具和模型。
保护凭据，不输出或保存 API 密钥；不要向无关外部人员发消息。

你自己必须持续做数学、审查和决策。给并行会话互补且具体、可验收的任务，
限定各自文件 prefix，避免改到彼此成果。不能直接接受“证明完成”的自报：
独立检查定义、符号、归一化、限序、量词、实际物理分支和 inherited hypotheses，
复算关键证书，区分普通书面证明、interval arithmetic、floating diagnostics 和 provenance。
所有尝试都记下来并比较，失败证据也要保留。

当前两条重点：

1. 平均提案的正性补全。第35轮已经证明：只要指定平均提案能保 mean/sector/mark
   补成非负，就能直接夹逼 theta，不需要另证 conic o(kappa)、UI 或 HR。
   第36轮已有所有实际场上的 O_tau(n^(5/4)) 一次反射补全深度，
   但对应长深度的 marked Cesaro 条件仍未证明。
   真正缺口是把补全和素数上的 marked arithmetic 衔接起来。
2. 复参数路线。第36轮已经证明实际标量分支的全纯延拓会自动控制 unwrapped phase
   和复增长，因此现在只需要 prime common cold–hot domain，不再有独立 growth 假设。
   这个共同冷域仍未证明；平方族有严格的实际 ramification 障碍。

特别注意：
有限正性记录不证明素数一致结论；保存的 Fourier-rounded 负例不等于 exact Picard
轨道反例，也不排除 eventual 成功或其他补全。
固定深度算术结果不能擅自延长到随场阶增长的深度。
平方阶不是素数猜想的反例，却是检验 field-general 捷径的必要对照。
第36轮末尾 transformed-Pick jet probe 尚未验收，不能当作已证结果。

优先推进真正的素数一致估计，不要只积累更多等价条件、无关小 family 障碍、
浮点优化或更长 prime 列表。若路线失败，给能改变下一步的严格证据并调整方向。
除非我暂停或更改目标，持续自主推进；已授权的并行和工具使用无需反复询问。
中文简洁汇报，进行中约每分钟更新重要发现。收尾必须说明已证、未证、
检验范围和下一步，不能把 ETH26 未解写成完成。
