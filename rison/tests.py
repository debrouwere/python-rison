# encoding: utf-8

if __name__ == '__main__':
    p = Parser()

    rison_examples = [
        "(a:0,b:1)",
        "(a:0,b:foo,c:'23skidoo')",
        "!t",
        "!f",
        "!n",
        "''",
        "0",
        "1.5",
        "-3",
        "1e30",
        "1e-30",
        "G.",
        "a",
        "'0a'",
        "'abc def'",
        "()",
        "(a:0)",
        "(id:!n,type:/common/document)",
        "!()",
        "!(!t,!f,!n,'')",
        "'-h'",
        "a-z",
        "'wow!!'",
        "domain.com",
        "'user@domain.com'",
        "'US $10'",
        "'can!'t'",
    ];

    for s in rison_examples:
        print
        print '*'*70
        print
        print s
        
        print '%r' % (p.parse(s),)