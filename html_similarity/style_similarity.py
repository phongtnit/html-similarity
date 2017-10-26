from parsel import Selector


# TODO: Improve performance: https://stackoverflow.com/questions/18348777/python-get-class-from-lxml-xpath
def get_classes(html):
    doc = Selector(text=html)
    classes = set(doc.xpath('//*[@class]/@class').extract())
    result = set()
    for cls in classes:
        for _cls in cls.split():
            result.add(_cls)
    return result


def jaccard_similarity(set1, set2):
    pass


def style_similarity(page1, page2):
    """

    A = classes(Document_1)
    B = classes(Document_2)

    style_similarity = |A & B| / (|A| + |B| - |A & B|)

    :param page1: html of the page1
    :param page2: html of the page2
    :return: Number between 0 and 1. If the number is next to 1 the page are really similar.
    """
    classes_page1 = get_classes(page1)
    classes_page2 = get_classes(page2)
    intersection = len(classes_page1 & classes_page2)
    denominator = len(classes_page1) + len(classes_page2) - intersection
    if denominator == 0:
        return 0
    return intersection / denominator