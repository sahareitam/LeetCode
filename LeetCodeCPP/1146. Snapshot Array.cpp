class SnapshotArray {
    int snap_id;
    vector<vector<pair<int,int>>>updates;
public:


    SnapshotArray(int length) {
        updates.resize(length);
        snap_id = 0;
    }


    void set(int index, int val) {
        if (!updates[index].empty() && updates[index].back().first == snap_id){
            updates[index].back().second = val;
        }else{
            updates[index].push_back({snap_id, val});
        }
    }
    int snap() {
        snap_id++;
        return snap_id-1;
    }

    int get(int index, int snap_id) {
        for(int i=updates[index].size()-1;i>=0;i--){
            if(updates[index][i].first <= snap_id){
                return updates[index][i].second;
            }
        }
        return 0;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */