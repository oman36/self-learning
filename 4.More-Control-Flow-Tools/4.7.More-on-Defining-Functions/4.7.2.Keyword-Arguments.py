def example(kind, *arguments, **keywords):
    print('kind = %s' % (kind,))

    for arg in arguments:
        print(arg)

    print("-" * 40)

    for kw in keywords:
        print(kw, ":", keywords[kw])