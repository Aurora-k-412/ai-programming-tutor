#AI 诊断逻辑模块（Mock 版本）

def analyze_code(code):
    #删除空格，方便进行简单的规则匹配
    normalized_code = code.replace(" ","")

    # 检测一种典型的数组越界风险
    if (
        "nums[i+1]" in normalized_code and "range(len(nums))" in normalized_code
    ):
        return{
            "error_type":"可能存在边界条件错误",
            "knowledge" :"列表索引",
            "analysis":"循环访问整个列表时，nums[i+1] 可能超出索引范围。",
            "hint":"思考一下，当i是最后一个元素的索引时，i+1是否仍然有效？"
        }

    # 没有匹配到当前演示规则
    return {
        "error_type": "未匹配到已知问题",
        "knowledge": "待进一步分析",
        "analysis": "当前模拟诊断模块尚未发现其支持识别的问题，但不代表代码一定正确。",
        "hint": "可以检查循环范围、边界条件和预期输出。"
    }
