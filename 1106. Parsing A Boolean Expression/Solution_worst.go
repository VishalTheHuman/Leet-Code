func parseBoolExpr(expression string) bool {
    if len(expression)== 1{
        return (expression == "t")
    }
    l := len(expression)
    switch expression[0:1] {
        case "&" :
            return and(expression[2:l-1])
        case "!":
            return not(expression[2:l-1])
        case "|":
            return or(expression[2:l-1])
    }
    return true
}

func process(expression string) []bool{
    store := []bool{}
    for i:=0;i<len(expression);i++{
        val := expression[i:i+1]
        if val==","{
            continue
        }
        temp := ""
        if val=="&" || val=="!" || val=="|" {
            count := 0
            temp += expression[i:i+1]
            i += 1
            for i<len(expression){
                chk := expression[i:i+1]
                if chk == "(" {
                    count++
                } else if chk == ")"{
                    count--
                }
                if count == 0 {
                    break
                }
                temp += chk
                i++
            }
        }
        
        var curr bool
        if temp !=""{
            switch val {
                case "&":
                    curr = and(temp[2:])
                case "|":
                    curr = or(temp[2:])
                case "!":
                    curr = not(temp[2:])
            }
        } else{
            curr = (val=="t")
        }
        store = append(store,curr)
    }
    return store
}

func and(expression string) bool {
    result := process(expression)
    for i:=1;i<len(result);i++{
        result[0]=result[0] && result[i]
    }
    return result[0]
}

func or(expression string) bool {
    result := process(expression)
    for i:=1;i<len(result);i++{
        result[0]= result[0] || result[i]
    }
    return result[0]
}

func not(expression string) bool {
    return !process(expression)[0]
}
