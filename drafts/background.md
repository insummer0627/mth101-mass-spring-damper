# Part 1 Background sample

已对照MTH101_CW.pdf第1–2页及Example Reports.pdf中弹簧系统示例（PDF第60–61页）核查。本文件包含Background讨论sample及交接说明，不是完整报告。内容保留原有AI辅助生成记录，未因本次语言与结构修订改变其来源。

## Background

Mechanical equipment can experience repeated forces during operation. Rotating imbalance is one source of vibration, and excessive vibration can contribute to wear or failure [1]. Understanding the response to periodic forcing is therefore relevant to engineering vibration analysis. A mass–spring–damper system provides a simple representation of inertia, elastic restoring forces and energy dissipation [2].

Educational treatments of forced vibration distinguish the transient motion associated with initial conditions from the steady periodic response maintained by an external force [2,3]. This distinction provides a basis for interpreting displacement over time and examining how damping affects the response. In this project, we consider a single-degree-of-freedom mass–spring–damper system subjected to a harmonic external force and described by a second-order ordinary differential equation.

Our aim is to investigate the displacement over time and compare responses when damping is varied while the other conditions remain fixed. We plan to compare analytical and numerical solutions under identical conditions to check the consistency of the calculations. This comparison does not validate the model against measurements from a particular machine. The investigation connects differential equations with an engineering vibration problem while making the model’s assumptions and limitations explicit.

## 中文理解和对接

第一段交代旋转不平衡与磨损等工程动机；第二段通过[2,3]说明瞬态与稳态的教材背景，再引入本组问题；第三段给出阻尼比较及解析数值对照的目标。研究范围沿用现有sample，仍由成员2和3确认；没有声称研究已经完成。

静平衡参考位置、弹簧线性、黏性阻尼、参数和初始条件应在Description of the model(s)中完整说明，Background不代替该部分。演示参数标注和仿真代码不作修改。

课程未规定Background单独词数；800–1000词适用于整篇正文。此sample约200词，需与其余章节共同控制总词数。模型推导与数学求解仍须在后续章节呈现，不能以背景和数值图表替代。

Example Reports用于参考“工程问题—数学工具—研究目的”的组织方式，不是强制模板或已核实文献来源。PDF第60页研究的是理想与实际弹簧的位移差异，本项目仍研究周期外力和阻尼，不引入锈蚀或附加质量等新主题。详细检查见[Background核查记录](../docs/background_review.md)。

## References

[1] University of Alberta. (n.d.). Classification of Vibrations. Engineering at Alberta Courses. https://engcourses-uofa.ca/books/vibrations-and-sound/introduction/classification-of-vibrations/

[2] University of Alberta. (n.d.). Damped Spring Mass System. Engineering at Alberta Courses. https://engcourses-uofa.ca/books/vibrations-and-sound/forced-vibrations-of-damped-single-degree-of-freedom-systems/damped-spring-mass-system/

[3] Massachusetts Institute of Technology. (2016). Lecture 3: Driven Oscillators, Transient Phenomena, Resonance. MIT OpenCourseWare, Physics III: Vibrations and Waves. https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-3/

## 候选方法资料

下列资料未在当前Background正文引用，不计入其正式References。成员4若确定使用拉普拉斯变换，可在实际方法说明中引用；不要把两种方法以上误写为强制要求。

Massachusetts Institute of Technology. (2011). Laplace Transform: Solving Initial Value Problems. MIT OpenCourseWare, Differential Equations. https://www.ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/resources/mit18_03scf11_s29_0intro/

网页访问核查日期：2026-10-29。编号为交接用格式，最终由成员6按课程要求统一。教学文献支持模型背景和方法，不提供本包的演示参数，也不是该模型对真实机器的实验验证。
