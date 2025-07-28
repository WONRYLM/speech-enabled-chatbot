from fpdf import FPDF

class PDF(FPDF):
    pass

pdf = PDF()
pdf.add_page()

# Register and use a Unicode-capable font
#pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "", r"C:\Users\USER\HelloWorld\DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=11)

# Make sure you have 'DejaVuSans.ttf' in the same folder or update the path
# You can download it from: https://dejavu-fonts.github.io/

content = """
🇰🇪 肯尼亚医疗机构走访总结报告

1. 内罗毕医院（Nairobi Hospital）
该院目前使用德国 STORZ（史托斯） 和日本 OLYMPUS（奥林巴斯） 的内窥镜设备。

医疗总监 Odede 先生的主要反馈与建议：
- 希望设备及技术人员可常驻当地，确保快速响应
- 要求设备具备 99% 的正常运行时间，保障手术流程连续性
- 附件及维修服务需实现本地化，降低维护周期与成本
- 期望为手术室工作人员提供专业的系统性培训

建议后续行动：
建议向 Odede 先生发出正式函件，简要介绍公司业务，并提议安排一场会议，由其召集实际设备使用者参与，便于深入了解临床需求和改进空间。

2. 帕克医疗中心（Park Medical Centre）
访谈对象：Njagi 医生
- 从业经验：10年，执业于内罗毕医院、阿迦汗医院、MP Shah医院
- 专业领域：腹腔镜手术、子宫内膜异位症、子宫切除术

重点关注：
- 产品质量与价格比
- 本地售后服务能力及精密器械的供应保障
- 市场已有竞争者（如印度品牌 Laryox）进入

Njagi 医生的合作建议：
1. 精准定位当前与潜在使用群体
2. 举办实操性研讨会（workshop）展示设备功能
3. 参与医学继续教育（CME）项目，提升专业曝光
4. 建立与关键专家的合作关系网络
5. 深入理解医生在使用过程中面临的痛点，并提出解决方案

市场策略建议：
- 初期聚焦 1~2 款核心产品，打造专业口碑
- 逐步扩大产品线，引导市场需求
- 加强品牌建设与可见度，强化市场影响力
- 与竞争产品深度对比，突出差异化价值主张

优先考虑的产品配置：
- 高清成像系统
- 性价比高的 3D 塔式系统
- 支持 4K 荧光成像的解决方案

3. Kigen 医生
- 从业资历：20年资深妇科专家
- 执业机构：私人诊所、内罗毕医院、Coptic、Karen、内罗毕妇女医院等多家大型医院

市场现状观察：
- Storz 设备广泛分布于：内罗毕医院、Aga Khan、Karen、Mater、Avenue、Nairobi West、Nairobi South 等医院
- Olympus 设备主要见于：Coptic、MP Shah、内罗毕医院、Aga Khan

采购方式：
- 一次性付款购置
- 分期付款方案（Hire Purchase）

核心需求：
- 设备质量稳定、价格合理
- 售后服务及时、专业
- 小型手术器械具备本地库存与供应能力

特别建议与合作机会：
1. 探讨引入CT、MRI、内窥镜等相关高端医疗影像设备
2. 考虑开发便携式腹腔镜设备，支持偏远地区义诊与公益医疗活动

承诺支持：
Kigen 医生愿主动联系其所在医疗网络中的专业人士，并协调召开用户座谈会，帮助我们收集更广泛的使用反馈，推动合作进程。

总结与建议

| 目标              | 建议举措                                                   |
|-------------------|------------------------------------------------------------|
| 建立信任与品牌曝光 | 主动拜访重点专家，组织小型沙龙、临床演示或CME合作课程    |
| 了解市场真实需求  | 与已有设备用户开展座谈会、收集一线反馈                    |
| 打开初期市场      | 聚焦高性价比的成像方案（如3D塔、4K系统）与本地化服务能力 |
| 长期布局策略      | 搭建售后与零部件本地支持体系，探索便携式与影像设备扩展线 |
"""

# Add content
pdf.multi_cell(0, 8, content)

# Save the file
pdf.output("肯尼亚医疗机构走访总结报告.pdf")

print("PDF saved as 肯尼亚医疗机构走访总结报告.pdf")
