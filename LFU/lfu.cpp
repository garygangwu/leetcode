#include <iostream>
#include <unordered_map>
#include <string>
#include <memory>
#include <list>

using namespace std;

class CacheEntry {
public:
  CacheEntry() {}

  CacheEntry(int key, string data) {
    key_ = key;
    data_ = data;
    freq_ = 0;
  }

  int key_;
  string data_;
  int freq_;
  list<int>::iterator freqListIter_;
  list<int>::iterator keysIter_;
};

class LFUCache {
public:
  LFUCache(int capacity) {
    capacity_ = capacity;
    evictionSize_ = max(2, (int)(capacity_ * 0.1));
    cout << "capacity: " << capacity_
         << ", evictionSize: " << evictionSize_ << endl;
  }

  ~LFUCache() {
  }

  void set(int key, string value) {
    if (cacheMap_.size() >= capacity_) {
      eviction();
    }

    auto iter = cacheMap_.find(key);
    if (iter == cacheMap_.end()) {
      CacheEntry entry(key, value);
      freqToKeys_[0].push_front(key);
      entry.keysIter_ = freqToKeys_[0].begin();
      if (freqList_.empty() || freqList_.front() != 0) {
        freqList_.push_front(0);
      }
      entry.freqListIter_ = freqList_.begin();
      cacheMap_[key] = entry;
    } else {
      iter->second.data_ = value;
      increaseFrequency(iter->second);
    }
  }

  string get(int key) {
    auto iter = cacheMap_.find(key);
    if (iter == cacheMap_.end()) {
      return "";
    }

    increaseFrequency(iter->second);
    return iter->second.data_;
  }


  void dump() {
    cout << endl;
    cout << "cache" << endl;
    for (const auto& iter : cacheMap_) {
      cout << iter.second.key_
           << " data: " << iter.second.data_
           << " freq: " << iter.second.freq_
           << " freqIter: " << *iter.second.freqListIter_
           << endl;
    }
    cout << "freqToKeys" << endl;
    for (const auto& iter : freqToKeys_) {
      cout << "freq: " << iter.first << " size: " << iter.second.size() << " : ";
      for (auto key : iter.second) {
        cout << key << " ";
      }
      cout << endl;
    }
    cout << "freqList: ";
    for (auto freq : freqList_) {
      cout << freq << " ";
    }
    cout << endl;
  }

private:
  void increaseFrequency(CacheEntry& entry) {
    int old_freq = entry.freq_;
    int new_freq = old_freq + 1;
    entry.freq_ = new_freq;

    // update freqToKeys_
    freqToKeys_[old_freq].erase(entry.keysIter_);

    // update freqList_ and find the new freq in freqList_
    list<int>::iterator newFreqIter;
    if (freqToKeys_[old_freq].empty()) {
      freqToKeys_.erase(old_freq);
      newFreqIter = freqList_.erase(entry.freqListIter_);
    } else {
      newFreqIter = entry.freqListIter_;
      ++newFreqIter;
    }
    if (newFreqIter == freqList_.end() || *newFreqIter != new_freq) {
      newFreqIter = freqList_.insert(newFreqIter, new_freq);
    }

    freqToKeys_[new_freq].push_front(entry.key_);

    entry.freqListIter_ = newFreqIter;
    entry.keysIter_ = freqToKeys_[new_freq].begin();
  }

  void eviction() {
    cout << "do eviction" << endl;
    int numToEvict = evictionSize_;
    while (numToEvict > 0) {
      int lowestFreq = freqList_.front();
      while (numToEvict > 0 && !freqToKeys_[lowestFreq].empty()) {
        int key = freqToKeys_[lowestFreq].back();
        freqToKeys_[lowestFreq].pop_back();
        cacheMap_.erase(key);
        cout << "Evict: " << key << endl;
        numToEvict--;
      }
      if (freqToKeys_[lowestFreq].empty()) {
        freqList_.pop_front();
      }
    }
  }

  unordered_map<int, CacheEntry> cacheMap_;
  unordered_map<int, list<int> > freqToKeys_;
  list<int> freqList_;
  int capacity_;
  int evictionSize_;
};

int main(int argc, char** argv) {
  LFUCache cache(6);
  cache.set(1, "ssss");
  cache.set(2, "aaaa");
  cache.set(3, "bbbb");
  cache.dump();
  cout << cache.get(1) << endl;
  cache.set(4, "cccc");
  cache.dump();
  cout << cache.get(3) << endl;
  cout << cache.get(3) << endl;
  cout << cache.get(3) << endl;
  cache.set(5, "dddd");
  cout << cache.get(2) << endl;
  cout << cache.get(5) << endl;
  cout << cache.get(4) << endl;
  cout << cache.get(5) << endl;
  cout << cache.get(4) << endl;
  cout << cache.get(5) << endl;
  cout << cache.get(4) << endl;
  cout << cache.get(5) << endl;
  cout << cache.get(4) << endl;
  cache.dump();
  cache.set(6, "gggg");
  cache.dump();
  cache.set(7, "hhhh");
  cache.dump();
  return 0;
}
