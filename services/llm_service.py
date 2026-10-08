#AI 诊断逻辑模块（Mock 版本）

def analyze_code(code):
    #删除空格，方便进行简单的规则匹配
    normalized_code = code.replace(" ","")

    if (
        "nums[i+1]" in normalized_code and "range(len(nums))" in normalized_code
    ):
        return{
            "error_type":"可能存在边界条件错误",
            "knowledge" :"列表索引",
            "analysis":"循环访问整个列表时，nums[i+1] 可能超出索引范围。",
            "hints":[
                    "思考一下，当i是最后一个元素的索引时，i+1是否仍然有效？",
                    "假设列表有4个元素，合法索引是0、1、2、3。当i=3时，i+1是多少？",
                    "尝试调整range()的循环范围，确保i+1始终小于len(nums)。"
            ]
        }

    # 没有匹配到当前演示规则
    return {
        "error_type": "未匹配到已知问题",
        "knowledge": "待进一步分析",
        "analysis": "当前模拟诊断模块尚未发现其支持识别的问题，但不代表代码一定正确。",
        "hints":[
            "先检查代码是否符合题目要求。",
            "尝试使用简单输入和边界情况进行测试。",
            "重点检查循环条件、变量变化和返回结果。"
        ]
    }
