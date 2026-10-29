# MTH101 

日期：2026-10-29。

## 通知
已完成Background英文讨论sample、核查过的文献链接，以及可运行的仿真演示。参数是自行设定的演示值，等模型组提交统一条件后再替换；目前不是最终项目结果。

请岗位2两位同学一起确认系统图、正方向、静平衡参考位置、假设、m/c/k的值和来源、外力表达式与单位、初始条件；
岗位3两位同学一起确认研究问题和每张图的比较指标；
岗位4提供经核查的推导及可计算解析式。
收到统一条件后更新代码和图表，交3和4复核，再把结果交6写结论并统一引用。

## 当前完成与依赖

|交付|状态|下一步|
|---|---|---|
|英文Background sample及中文说明|已提供讨论版|2核对工程场景，3核对研究承诺|
|文献与引用用途|网页已核查|6按课程格式统一|
|仿真源码、数据、图表、误差记录|已生成演示版|2提供参数，4确认解析式，3和4审核|
|课程适配|已核对原始任务书与示例|全文和最终研究范围仍待组内审核|
|真实设备验证|没有实验数据|不可将数值一致称为真实实验验证|

## 课程要求适配

已核对MTH101_CW.pdf第1页：正文800–1000词，包含Background、Description of the model(s)、Explanation of the solutions、Conclusion、References；方程、图与参考文献列表不计入正文。任务书第2页要求一组提交一份报告，封面列全员姓名和学号。Background核查见[检查记录](../../docs/background_review.md)。

建议正文约900词：Background约200，Model约200，Solutions约350，Conclusion约150。该分配为建议，不是课程要求。../../drafts/background.md的英文部分约200词。两张核心图已足以支持当前建议范围；频率响应图是选做，不为凑数而加入。

## 统一条件建议

演示方程：m x'' + c x' + k x = F0 cos(omega t)，t >= 0；x为向右、相对静平衡位置的位移。假设质量集中、弹簧线性、阻尼力与速度成正比、参数恒定、单向运动、固定支座，不考虑非线性和其他振型。外力是直接施加于质量的力，不是地面位移输入。

|量|演示值|单位|来源|
|---|---:|---|---|
|m|1|kg|自行设定，待2确认|
|c|0.8|N s/m|自行设定，待2确认|
|k|4|N/m|自行设定，待2确认|
|F0|1|N|自行设定，待2确认|
|omega|1.5|rad/s|自行设定，约0.239 Hz|
|相位及起始|0；t0=0|rad；s|自行设定|
|x(0)，x'(0)|0，0|m；m/s|自行设定|
|计算时间|0–30|s|演示设置|
|基础步长|0.01|s|固定步长RK4；另以0.005复算|

演示阻尼比较c=0.4、0.8、1.6，其余量及初值固定；均为欠阻尼。没有覆盖临界或过阻尼案例。

## 成员5计算依据与图注

欠阻尼公式仅适用于m>0、k>0、0<c<2 sqrt(mk)。令alpha=c/(2m)，wd=sqrt(k/m-alpha²)，D=k-m omega²，Q=D²+(c omega)²，a=F0 D/Q，b=F0 c omega/Q。

x_ss=a cos(omega t)+b sin(omega t)；C=x0-a，E=(v0-b omega+alpha C)/wd。

x(t)=x_ss+exp(-alpha t)[C cos(wd t)+E sin(wd t)]。

数值系统为x'=v，v'=(F0 cos(omega t)-cv-kx)/m。源码独立使用固定步长四阶Runge–Kutta积分，再与上述公式对照。公式是本演示的参考式，仍需岗位4自行推导和核对；不是对其尚未交付推导的验收。

Figure 1. Analytical and RK4 displacement responses for the illustrative parameter set. The steady periodic component is shown separately; the lower panel displays the numerical error. All parameters are demonstration values.

图1回答相同条件下数值与解析是否一致，以及总响应如何趋近稳态。误差单位为m；误差小只支持本算例的计算一致性。metrics.json记录两种步长的最大绝对误差、初值检查和方程残差。

Figure 2. Effect of damping on displacement under the same harmonic force. Only c is varied; m, k, F0, omega and the initial conditions are held fixed. All parameters are demonstration values.

图2同时画早期0–12s和后期20–30s，避免把瞬态峰值当作稳态幅值。本演示的稳态幅值为F0/sqrt((k-m omega²)²+(c omega)²)，本频率下随正阻尼增大而减小；不能据此声称任意瞬态峰值均单调下降。更不能把欠阻尼自由衰减的临界分类直接当作受迫稳态是否振荡的判断。

若加频率扫描，应保持F0固定并说明。这属于恒力幅频率响应；真实旋转不平衡力幅值可能随转速平方变化，不能直接把同一曲线解释为实际机器转速扫描。

## 运行与替换

Python 3运行：python simulation_sample.py。仅用标准库，无需安装第三方库；输出位置为脚本同目录的simulation文件夹。打开sample_preview.html可读英文sample并看图。SVG可直接插入支持矢量图的排版软件；CSV保留全部时间采样点。

改脚本顶部参数后需重新运行并更新统一条件表、图注、Background研究承诺、误差记录与结论；脚本会拒绝欠阻尼公式以外的条件。最终交6前，3和4需确认图意、解析适用条件、单位和数值结果。
