import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      home: Container(
        padding: EdgeInsets.all(20),
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.red, Colors.blue],
            begin: AlignmentGeometry.topLeft,
            end: AlignmentGeometry.bottomRight,
          ),
        ),
        child: Column(
          children: [
            Container(
              margin: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 20),
              child: Center(
                child: Text(
                  'Axborot xavfsizligini boshqarish',
                  style: TextStyle(color: Colors.white, fontSize: 20),
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  color: Colors.blue,
                  width: MediaQuery.of(context).size.width * 0.29,
                  height: 150,
                  child: Center(
                    child: Text('1', style: TextStyle(color: Colors.white)),
                  ),
                ),
                Container(
                  color: Colors.blue,
                  width: MediaQuery.of(context).size.width * 0.29,
                  height: 150,
                  child: Center(
                    child: Text('2', style: TextStyle(color: Colors.white)),
                  ),
                ),
                Container(
                  color: Colors.blue,
                  width: MediaQuery.of(context).size.width * 0.29,
                  height: 150,
                  child: Center(
                    child: Text('3', style: TextStyle(color: Colors.white)),
                  ),
                ),
              ],
            ),
            Container(
              margin: EdgeInsets.symmetric(vertical: 20),
              color: Colors.green,
              height: 150,
              child: Center(
                child: Text('4', style: TextStyle(color: Colors.white)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
