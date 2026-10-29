# Part 1 Background sample

学习与小组讨论示例。课程原始任务书尚未提供；仓库记载AI仅可语言润色，因此请核实允许范围，不要把本示例当作本人独立写作直接提交。以下按英文报告第一部分Background理解，不是完整报告。

## Background

Mechanical equipment can experience repeated forces during operation. Rotating imbalance is one source of vibration, and excessive vibration can contribute to wear or failure [1]. A mass–spring–damper system provides a simple way to study this behaviour: the mass represents inertia, the spring provides a restoring force, and the damper represents energy dissipation [2].

This project considers a single degree of freedom system subjected to a harmonic external force. The displacement is measured from the static equilibrium position. With a linear spring and viscous damping, the motion is described by a second order ordinary differential equation [2]. The model allows us to distinguish the transient motion associated with the initial conditions from the steady periodic response maintained by the external force [2,3].

Our aim is to investigate the displacement over time and how it changes when damping is varied while the other conditions remain fixed. We plan to compare an analytical solution with a numerical solution under identical conditions. This comparison checks the consistency of the calculations; it does not establish that the model accurately predicts a particular machine. The study therefore connects differential equations with an engineering vibration problem while keeping the assumptions and limitations explicit.

## 中文理解和对接

第一段说明工程动机和三个元件的含义；第二段确定单自由度、静平衡参考位置、线性弹簧和黏性阻尼；第三段提出时间响应、阻尼比较以及解析数值对照的研究目的。这里的研究范围是建议，成员2和3需要确认。

没有把拉普拉斯变换写成已完成的方法。成员4若确定使用拉普拉斯变换，再把第三段第二句改为：We plan to use the Laplace transform to solve the initial value problem and compare the result with a numerical solution under identical conditions. 并引用[4]。

## References

[1] University of Alberta. (n.d.). Classification of Vibrations. Engineering at Alberta Courses. https://engcourses-uofa.ca/books/vibrations-and-sound/introduction/classification-of-vibrations/

[2] University of Alberta. (n.d.). Damped Spring Mass System. Engineering at Alberta Courses. https://engcourses-uofa.ca/books/vibrations-and-sound/forced-vibrations-of-damped-single-degree-of-freedom-systems/damped-spring-mass-system/

[3] Massachusetts Institute of Technology. (2016). Lecture 3: Driven Oscillators, Transient Phenomena, Resonance. MIT OpenCourseWare, Physics III: Vibrations and Waves. https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-3/

[4] Massachusetts Institute of Technology. (2011). Laplace Transform: Solving Initial Value Problems. MIT OpenCourseWare, Differential Equations. https://www.ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/resources/mit18_03scf11_s29_0intro/

网页访问核查日期：2026-10-29。编号为交接用格式，最终由成员6按课程要求统一。教学文献支持模型背景和方法，不提供本包的演示参数，也不是该模型对真实机器的实验验证。
