import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mindrushflutter/main.dart'; // Asegúrate de que la ruta sea correcta

void main() {
  testWidgets('Registro Page has a title and a button', (WidgetTester tester) async {
    await tester.pumpWidget(MyApp());

    // Verifica que el título esté presente
    expect(find.text('Registro'), findsOneWidget);
    // Verifica que el botón de registrar esté presente
    expect(find.text('Registrar'), findsOneWidget);
  });
}