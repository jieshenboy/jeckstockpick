import MySQLdb

class savebooksData(object):
    def __init__(self,items):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'crawlUSER'
        self.passwd = 'crawl123'

        self.db = 'bs4DB'

        self.run(self,items)

    def run(self, items):
        print("1")
        conn = MySQLdb.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.passwd,
            db = self.db,
            charset = 'utf8'
        )
        print("2")
        cur = conn.cursor()
        for item in items:
            print("3")
            cur.execute("INSERT INTO MV(top_num, score, mvName, singer,releasTime) VALUES (%s %s %s %s, %s)" %(item.top_num,
                                                                                                               item.score,
                                                                                                               item.mvName,
                                                                                                               item.singer,
                                                                                                               item.releasTime))
        cur.close()
        conn.commit()
        conn.close()

if __name__=="__main__":
    pass