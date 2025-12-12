import ctypes

class ClListHeadT(ctypes.Structure):
    pass
ClListHeadT._fields_ = [
    ("pNext", ctypes.POINTER(ClListHeadT)),
    ("pPrev", ctypes.POINTER(ClListHeadT)),
]

def CL_LIST_HEAD_EMPTY(head):
    return ctypes.addressof(head.pNext.contents) == ctypes.addressof(head)

def CL_LIST_HEAD_INIT(head):
    head.pPrev = ctypes.pointer(head)
    head.pNext = ctypes.pointer(head)

def __CL_LIST_ADD(element,prev,next):
    element.pNext = ctypes.pointer(next)
    element.pPrev = ctypes.pointer(prev)
    prev.pNext = ctypes.pointer(element)
    next.pPrev = ctypes.pointer(element)

def __CL_LIST_DEL(prev,next):
    prev.pNext = ctypes.pointer(next)
    next.pPrev = ctypes.pointer(prev)

def clListAdd(element, head):
    next = head.pNext.contents
    __CL_LIST_ADD(element, head, next)

def clListAddTail(element, head):
    prev = head.pPrev.contents
    __CL_LIST_ADD(element, prev, head)

def clListDel(element):
    try:
        prev = element.pPrev.contents
        next = element.pNext.contents
    except ValueError:
        return
    __CL_LIST_DEL(prev, next)
    element.pNext = ctypes.POINTER(ClListHeadT)()
    element.pPrev = ctypes.POINTER(ClListHeadT)()

def clListDelInit(element):
    clListDel(element)
    CL_LIST_HEAD_INIT(element)

def clListMoveInit(source, dest):
    if ctypes.addressof(source) == ctypes.addressof(dest) and not CL_LIST_HEAD_EMPTY(source):
        pFirst = source.pNext
        pLast = source.pPrev

        destPrev = dest.pPrev.contents
        destPrev.pNext = pFirst

        first = pFirst.contents
        first.pPrev = dest.pPrev

        last = pLast.contents
        last.pNext = dest

        dest.pPrev = pLast

        CL_LIST_HEAD_INIT(source)

