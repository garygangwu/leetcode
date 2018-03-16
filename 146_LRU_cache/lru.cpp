#include <iostream>
#include <unordered_map>
#include <string>
#include <list>

using namespace std;

class CacheEntry {
public:
  CacheEntry() {};

  CacheEntry(int key, const string& value, list<int>::iterator iter) {
    key_ = key;
    value_ = value;
    iter_ =  iter;
  }

  int key_;
  string value_;
  list<int>::iterator iter_;
};

class LRUCache {
public:
  LRUCache(int capacity) {
    if (capacity > 0) {
      capacity_ = capacity;
    } else {
      capacity_ = 10;
    }
  }

  void set(int key, string value) {
    if (cache_.size() >= capacity_) {
      eviction();
    }

    auto iter = cache_.find(key);
    if (iter == cache_.end()) {
      recentKeyList.push_front(key);
      CacheEntry entry(key, value, recentKeyList.begin());
      cache_[key] = entry;
    } else {
      iter->second.value_ = value;
      recentKeyList.erase(iter->second.iter_);
      recentKeyList.push_front(key);
      iter->second.iter_ = recentKeyList.begin();
    }
  }

  bool get(int key, string* value) {
    auto iter = cache_.find(key);
    if (iter == cache_.end()) {
      return false;
    }

    *value = iter->second.value_;
    recentKeyList.erase(iter->second.iter_);
    recentKeyList.push_front(key);
    iter->second.iter_ = recentKeyList.begin();
    return true;
  }

  void dump() {
    cout << "dump:" << endl;
    for (int key : recentKeyList) {
      auto iter = cache_.find(key);
      cout << iter->second.key_ << " : " << iter->second.value_ << endl;
    }
  }

private:
  void eviction() {
    while (cache_.size() >= capacity_) {
      int key = recentKeyList.back();
      cache_.erase(key);
      recentKeyList.pop_back();
    }
  }

  unordered_map<int, CacheEntry> cache_;
  list<int> recentKeyList;
  int capacity_;
};

int main(int argc, char** argv) {
  LRUCache cache(4);
  cache.set(1, "ssss");
  cache.set(2, "bbbb");
  cache.set(3, "cccc");
  cache.set(4, "dddd");
  string value;
  bool ret = cache.get(2, &value);
  cout << ret << " " << value << endl;
  cache.dump();
  cache.set(1, "aaaaa");
  cache.dump();
  cache.set(5, "eeee");
  cache.dump();

  value = "";
  ret = cache.get(3, &value);
  cout << ret << " " << value << endl;

  value = "";
  ret = cache.get(4, &value);
  cout << ret << " " << value << endl;

  cache.set(6, "ffff");
  cache.dump();
  return 0;
}
