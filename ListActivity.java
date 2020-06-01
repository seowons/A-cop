package com.github.dudgns0507.keras;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

import java.util.ArrayList;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnTextChanged;

public class ListActivity extends AppCompatActivity {
    private static final String TAG = ListActivity.class.getSimpleName();

    private ListViewAdapter adapter;
    private ArrayList<Data> dataList;

    @BindView(R.id.search_edit)
    EditText searchEdit;
    @BindView(R.id.list_view)
    ListView listView;

    // 검색 텍스트 변경시 이벤트
    @OnTextChanged(R.id.search_edit) void onTextChanged() {
        String search = searchEdit.getText().toString().trim();

        // 리스트 초기화 후 검색 텍스트가 포함된 결과만 추가
        adapter.cleanAll();

        for (int i = 0; i < dataList.size(); i++) {
            if(dataList.get(i).getName().contains(search)) {
                adapter.addItem(dataList.get(i));
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list);

        ButterKnife.bind(this);

        // 리스트 초기화
        adapter = new ListViewAdapter(this);
        listView.setAdapter(adapter);

        // 리스트 클릭 이벤트
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                // 리스트 클릭시 결과 액티비티 호출해서 정보 표시
                Intent intent = new Intent(ListActivity.this, ResultActivity.class);
                intent.putExtra("result", adapter.getItem(position).getId());
                startActivity(intent);
            }
        });

        // 상품 데이터들 리스트에 추가
        dataList = new ArrayList<Data>();
        dataList.add(new Data(0, "비비고 왕교자", R.drawable.dumpling, 0));
        dataList.add(new Data(1, "모짜렐라 핫도그", R.drawable.hotdog, 0));
        dataList.add(new Data(2, "대림 부산어묵", R.drawable.fishcake, 0));
        dataList.add(new Data(3, "지도표성경 올리브&녹차김", R.drawable.laver, 0));
        dataList.add(new Data(4, "큐원홈메이드 씨앗호떡믹스", R.drawable.pancake, 0));
        dataList.add(new Data(5, "토마토와 생크림 로제", R.drawable.pasta, 0));
        dataList.add(new Data(6, "스팸 클래식", R.drawable.spam, 0));
        dataList.add(new Data(7, "동원참치 라이트 스탠다드", R.drawable.tuna, 0));
        dataList.add(new Data(8, "튀김 우동 컵", R.drawable.udon, 0));
        dataList.add(new Data(9, "햇반", R.drawable.rice, 0));
        dataList.add(new Data(10, "신라면", R.drawable.ramen, 0));
        dataList.add(new Data(11, "삼계탕", R.drawable.chickensoup, 0));
        dataList.add(new Data(12, "우리쌀 구운마늘크림수프", R.drawable.soup, 0));
        dataList.add(new Data(13, "풀무원 부드러운 찌개 두부", R.drawable.tofu, 0));
        dataList.add(new Data(14, "생가득 새콤달콤 유부초밥", R.drawable.tofusushi, 0));
        dataList.add(new Data(15, "닭가슴살 블랙페퍼", R.drawable.breast, 0));
        dataList.add(new Data(16, "3분 쇠고기 카레", R.drawable.curry, 0));
        dataList.add(new Data(17, "다향 훈제오리", R.drawable.duck, 0));
        dataList.add(new Data(18, "비비고 버터간장 김자반", R.drawable.jaban, 0));
        dataList.add(new Data(19, "황도 통조림", R.drawable.peachcan, 0));

        // 리스트 데이터 리스트뷰에 추가
        for (int i = 0; i < dataList.size(); i++) {
            adapter.addItem(dataList.get(i));
        }
    }

    // 리스트뷰 표시를 위한 어댑터
    public class ListViewAdapter extends BaseAdapter {
        class ViewHolder {
            @BindView(R.id.thumbnail_img)
            ImageView thumbnailImg;
            @BindView(R.id.name_text)
            TextView nameText;

            public ViewHolder(View view) {
                ButterKnife.bind(this, view);
            }
        }

        private Context mContext = null;
        private ArrayList<Data> mListData = new ArrayList<Data>();

        public ListViewAdapter(Context mContext) {
            super();
            this.mContext = mContext;
        }

        @Override
        public int getCount() {
            return mListData.size();
        }

        @Override
        public Data getItem(int position) {
            return mListData.get(position);
        }

        @Override
        public long getItemId(int position) {
            return position;
        }

        @Override
        public View getView(final int position, View convertView, ViewGroup parent) {
            ViewHolder holder;

            if (convertView == null) {
                LayoutInflater inflater = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
                convertView = inflater.inflate(R.layout.list_item, null);

                holder = new ViewHolder(convertView);
                convertView.setTag(holder);
            } else {
                holder = (ViewHolder) convertView.getTag();
            }

            // 리스트뷰에 데이터 바인딩
            Data mData = mListData.get(position);

//            Glide.with(mContext).load(mData.getDrawable()).into(holder.thumbnailImg);
            holder.nameText.setText(mData.getName());

            return convertView;
        }

        // 리스트뷰 아이템 추가
        public void addItem(Data data) {
            mListData.add(data);
            dataChange();
        }

        // 리스트뷰 아이템 삭제
        public void remove(int position) {
            mListData.remove(position);
            dataChange();
        }

        // 리스트뷰 데이터 변경시 호출
        public void dataChange() {
            notifyDataSetChanged();
        }

        // 리스트뷰 데이터 초기화
        public void cleanAll() {
            mListData.clear();
            dataChange();
        }
    }
}
