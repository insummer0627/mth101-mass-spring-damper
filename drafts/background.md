# Background — discussion draft

> 状态：待小组审核，非提交定稿。此版本来自此前聊天中的AI生成及修改文本，尚未经作者独立重写。课程文件仅允许AI语言润色；请按实际情况处理使用声明，并核查课程要求。研究范围与仿真承诺也需全组确认。

Mechanical equipment often experiences repeated forces during operation. For example, an unbalanced rotating component can produce a periodic force [1,2]. This can cause unwanted vibration, which may increase wear and lead to mechanical failure [1]. Studying this behaviour helps us understand why vibration needs to be considered in engineering.

In this project, we study a mass–spring–damper system under a harmonic external force. It is a simplified model rather than a complete description of a real machine. We focus on how the motion changes over time, including the initial transient response and the steady-state response [3]. We also examine how the forcing frequency affects the vibration.

We describe the system using an ordinary differential equation and use the Laplace transform to solve it with given initial conditions [4]. We then use Python to calculate a numerical solution and compare it with the analytical result. The graphs help us explain the response more clearly. Finally, we discuss the model’s limitations and the differences between this simple model and real equipment.

## References — verify before submission

[1] University of Alberta (n.d.). *Classification of Vibrations*. https://engcourses-uofa.ca/books/vibrations-and-sound/introduction/classification-of-vibrations/

[2] University of Alberta (n.d.). *Simple Spring–Mass System*. https://engcourses-uofa.ca/books/vibrations-and-sound/forced-vibrations-of-undamped-single-degree-of-freedom-systems/9155-2/

[3] Massachusetts Institute of Technology (2016). *Lecture 3: Driven Oscillators, Transient Phenomena, Resonance*. MIT OpenCourseWare. https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-3/

[4] Massachusetts Institute of Technology (2011). *Laplace Transform: Solving Initial Value Problems*. MIT OpenCourseWare. https://www.ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/resources/mit18_03scf11_s29_0intro/

## Review checklist

- [ ] 成员2确认工程背景与外力设定一致。
- [ ] 成员3确认瞬态、稳态和频率影响属于实际研究范围。
- [ ] 成员4确认解析工作与本文承诺一致。
- [ ] 成员5确认Python数值对照工作可完成。
- [ ] 成员6核查引用信息与格式。
- [ ] 由作者独立完成符合课程要求的提交稿，并如实记录AI使用。
