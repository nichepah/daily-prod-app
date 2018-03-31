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
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Iterator;

public class DisplayDataBSP extends AppCompatActivity {

    //ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_data_bsp);

        //listView = findViewById(R.id.listView);
        getJSON("http://10.151.7.169/php/sail/bsp_json.php");
    }

    /**  BEGINNING OF TEST IMPLEMENTATION WITH TEXTVIEW
    public void getJSON(final String urlWebService) {
        class GetJSON extends AsyncTask<Void, Void, String> {
            @Override
            protected void onPreExecute(){
                super.onPreExecute();
            }

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

                try {
                    JSONObject jsonObject = new JSONObject(json);
                    //String[] pData = new String[jsonObject.length()];
                    //JSONObject json2 = jsonObject.getJSONObject("results");
                    //pData[1] = (String) jsonObject.get("Sinter");
                    String sinter = jsonObject.getString("Sinter");
                    String productionDate = jsonObject.getString("Production_Date");
                    String ovenPushing = jsonObject.getString("Oven_Pushing");
                    String hm = jsonObject.getString("HM");
                    String pi = jsonObject.getString("PI");
                    String cs = jsonObject.getString("CS");
                    String sms1 = jsonObject.getString("SMS_1");
                    String sms2 = jsonObject.getString("SMS_2_CC");

                    String bbmIngotRolling = jsonObject.getString("BBM_ingot_rolling");
                    String rails = jsonObject.getString("Rails");
                    String urm = jsonObject.getString("URM");
                    String mm = jsonObject.getString("MM");
                    String wrm = jsonObject.getString("WRM");
                    String plateMill = jsonObject.getString("Plate_Mill");
                    String brm = jsonObject.getString("BRM");
                    String semis = jsonObject.getString("Semis");
                    String finSteel = jsonObject.getString("Fin_Steel");
                    String ssProd = jsonObject.getString("SS_Prod");
                    String ssDesp = jsonObject.getString("SS_Desp");

                    //Log.e("onLoadIntoListView", sinter + productionDate);

                    TextView textViewDate = findViewById(R.id.textView_Date);
                    textViewDate.setText("Date : "+productionDate);

                    TextView textViewOven = findViewById(R.id.textView_Oven);
                    textViewOven.setText("Ovens Push. : "+ovenPushing);

                    TextView textViewSinter = findViewById(R.id.textView_Sinter);
                    textViewSinter.setText("Sinter (T) : "+sinter);

                    TextView textViewHM = findViewById(R.id.textView_HM);
                    textViewHM.setText("Hot Metal (T) : "+hm);

                    TextView textViewPi = findViewById(R.id.textView_PI);
                    textViewPi.setText("Pig Iron (T) : "+pi);

                    TextView textViewCs = findViewById(R.id.textView_cs);
                    textViewCs.setText("Crude Steel (T) : "+cs);

                    TextView textViewSms1 = findViewById(R.id.textView_sms1);
                    textViewSms1.setText("SMS1 (T) : "+sms1);

                    TextView textViewSms2 = findViewById(R.id.textView_sms2);
                    textViewSms2.setText("SMS2 CC (T) : "+sms2);

                    TextView textViewBbm = findViewById(R.id.textView_bbm);
                    textViewBbm.setText("BBM Ingot (T) : "+bbmIngotRolling);

                    TextView textViewRails = findViewById(R.id.textView_Rails);
                    textViewRails.setText("Rails (T) : "+rails);

                    TextView textViewUrm = findViewById(R.id.textView_urm);
                    textViewUrm.setText("URM (T) : "+urm);

                    TextView textViewMm = findViewById(R.id.textView_mm);
                    textViewMm.setText("Merchant Mill (T) : "+mm);

                    TextView textViewWrm = findViewById(R.id.textView_wrm);
                    textViewWrm.setText("Wire Rod Mill (T) : "+wrm);

                    TextView textViewPlateMill = findViewById(R.id.textView_platemill);
                    textViewPlateMill.setText("Plate Mill (T) : "+plateMill);

                    TextView textViewBrm = findViewById(R.id.textView_brm);
                    textViewBrm.setText("BRM (T) : "+brm);

                    TextView textViewSemis = findViewById(R.id.textView_semis);
                    textViewSemis.setText("Semis (T) : "+semis);

                    TextView textViewFinSteel = findViewById(R.id.textView_finsteel);
                    textViewFinSteel.setText("Finished Steel (T) : " + finSteel);

                    TextView textViewSSProd = findViewById(R.id.textView_ssProd);
                    textViewSSProd.setText("Saleable Steel Produced (T) : "+ssProd);

                    TextView textViewSSDesp = findViewById(R.id.textView_ssDesp);
                    textViewSSDesp.setText("Saleable Steel Dispatched (T) : "+ssDesp);

                } catch (JSONException e) {
                    e.printStackTrace();
                }
                //Toast.makeText(getApplicationContext(), pData[1], Toast.LENGTH_LONG).show();
                //
            }
        }//end of class definition for GetJSON
        GetJSON getJSON = new GetJSON();
        getJSON.execute();
    }
    **/ /**END OF TEST IMPLEMENTATION WITH TEXTVIEW **/

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
                        super(context, R.layout.layout_row_bsp, keyarray);

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
                        View rowView = inflater.inflate(R.layout.layout_row_bsp, parent, false);
                        TextView keyTextView1 = rowView.findViewById(R.id.keyTextViewBSP);
                        TextView valTextView2 = rowView.findViewById(R.id.valTextViewBSP);
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
                            CustomListAdapter myAdapter = new CustomListAdapter(DisplayDataBSP.this, jsonKeys, jsonVals, imageIds);
                            //myAdapter.printVal();
                            ListView listView = findViewById(R.id.listViewBSP);
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
