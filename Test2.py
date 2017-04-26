__author__ = 'cjsvndtjs1@naver.com'

def urlParser(url):
    url_list = url.split('/')
    print url_list
    print 'Number of elements separated by \'/\': %d' %len(url_list)

    host = url_list[2]
    naver_id = url_list[3]
    post_num = url_list[4]

    print 'Host: %s \tID: %s\tPost Number: %s' %(host,naver_id,post_num)

if __name__ == '__main__':
    url = 'http://blog.naver.com/cjsvndtjs1/220988116746'

    urlParser(url)