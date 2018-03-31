package com.example.pa.sailproduction;

import android.app.Activity;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;

public class DisplayDataSSP extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_data_ssp);

        // get data
        getJSON("http://10.151.7.169/php/sail/ssp_json.php");
    }

    public void getJSON(final String urlWebService) {
        class GetJSON extends AsyncTask<Void, Void, String> {
            @Override
            protected void onPreExecute(){
                super.onPreExecute();
            }

            //private Context context;

            @Override
            protected String doInBackground(Void... voids) {
                try{
                    URL url = new URL(urlWebService);
                    HttpURLConnection con = (HttpURLConnection) url.openConnection();
                    StringBuilder sb = new StringBuilder();
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(con.getInputStream()));
                    String json;
                    while ((json = bufferedReader.readLine()) != null) {
                        sb.append(json + "\n");
                    }
                    //Log.e("InBackground", sb.toString().trim());
                    return sb.toString().trim();
                } catch (Exception e) {
                    return null;
                }

            } // end of doInBackground

            @Override
            protected void onPostExecute(String s){
                //Log.e("onPostExecute", s);
                super.onPostExecute(s);
                try{
                    //Toast.makeText(getApplicationContext(), "something", Toast.LENGTH_LONG).show();
                    loadTextViews(s);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }

            private void loadTextViews(String json) throws JSONException {

                /* Create a class within loadTextViews function, to create CustomListAdapter*/
                class CustomListAdapter extends ArrayAdapter {

                    private final Activity context;

                    private final Integer[] imageIDArray;

                    private final String[] keyArray;

                    private final String[] valArray;


                    public CustomListAdapter(Activity context, String[] keyarray, String[] valarray, Integer[] imageidarray) {
                        super(context, R.layout.layout_row_ssp, keyarray);

                        this.context = context;
                        this.keyArray = keyarray;
                        this.valArray = valarray;
                        //Log.e("CustomListAdapter constructor", );
                        this.imageIDArray = imageidarray;
                    }

                    public void printVal() {
                        Log.e("printVal from CustomListAdapter", "keyArray len " + keyArray.length);
                    }

                    public View getView(int position, View view, ViewGroup parent) {
                        LayoutInflater inflater = LayoutInflater.from(context);
                        View rowView = inflater.inflate(R.layout.layout_row_ssp, parent, false);
                        TextView keyTextView1 = rowView.findViewById(R.id.keyTextViewSSP);
                        TextView valTextView2 = rowView.findViewById(R.id.valTextViewSSP);
                        //ImageView imageView = findViewById(R.id.imageView);

                        //set the values
                        keyTextView1.setText(keyArray[position]);
                        valTextView2.setText(valArray[position]);
                        //imageView.setImageResource(imageIDArray[position]);
                        return(rowView);
                    }
                } // End of Class CustomListAdapter


                try {
                    /** */
                    JSONObject jsonObject = new JSONObject(json);

                    final String[] jsonKeys = new String[jsonObject.length()];
                    final String[] jsonVals = new String[jsonObject.length()];
                    final Integer[] imageIds = new Integer[jsonObject.length()];

                    Iterator<String> keysIter =  jsonObject.keys();
                    int i =0;
                    while ( keysIter.hasNext() ){
                        String key = keysIter.next();
                        String val = jsonObject.getString(key);
                        jsonKeys[i] = key;
                        jsonVals[i] = val;
                        //imageIds[i] = R.mipmap.icon_dsp_round;
                        //getResources().getIdentifier("icon_dsp", "drawable", getPackageName());

                        Log.e("onLoadIntoListView", jsonKeys[i] +" :: " + jsonVals[i] + "::" + imageIds[i]);

                        i++;
                    }
                    //ArrayAdapter <String> arrayAdapter = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, jsonKeys);
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            CustomListAdapter myAdapter = new CustomListAdapter(DisplayDataSSP.this, jsonKeys, jsonVals, imageIds);
                            //myAdapter.printVal();
                            ListView listView = findViewById(R.id.listViewSSP);
                            listView.setAdapter(myAdapter);
                        }
                    });

                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }

        }//end of class definition for GetJSON

        GetJSON getJSON = new GetJSON();
        getJSON.execute();
    }

}
