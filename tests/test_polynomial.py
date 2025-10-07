import sys
import os
import subprocess
import tempfile
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from polynomial import evaluate_polynomial


def test_example_polynomial():
    result = evaluate_polynomial(3, 2, -7, 5, 2, -1)
    assert result == 3  


def test_basic_polynomial():
    result = evaluate_polynomial(1, 1, 3, 2)
    assert result == 5


def test_loop_functionality():
    result1 = evaluate_polynomial(2, 3, 1, 2, 1)
    assert result1 == 16 
    
    result2 = evaluate_polynomial(1, 5, 10, 2)
    assert result2 == 20


def test_interactive_loop():
    input_sequence = "3\n2\n-7\n5\n2\n-1\ny\n1\n1\n3\n2\nn\n"
    
    result = subprocess.run(
        [sys.executable, "polynomial.py"],
        input=input_sequence,
        text=True,
        capture_output=True,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    
    assert result.returncode == 0
    
    output = result.stdout
    assert "-7" in output or "-7.0" in output
    assert "3" in output or "3.0" in output  
    assert "11" in output or "11.0" in output
    assert "5" in output or "5.0" in output


def test_interactive_loop_exit_immediately():
    """Test the interactive loop when user chooses 'n' immediately."""
    input_sequence = "2\n3\n1\n2\n1\nn\n"
    
    result = subprocess.run(
        [sys.executable, "polynomial.py"],
        input=input_sequence,
        text=True,
        capture_output=True,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    
    assert result.returncode == 0
    
    output = result.stdout
    assert "1" in output or "1.0" in output
    assert "7" in output or "7.0" in output
    assert "16" in output or "16.0" in output 


if __name__ == "__main__":
    test_functions = [
        test_example_polynomial,
        test_basic_polynomial,
        test_loop_functionality,
        test_interactive_loop,
        test_interactive_loop_exit_immediately
    ]
    
    print("Running polynomial evaluation tests...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
    
    print("=" * 50)
    print(f"Tests completed: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("All tests passed! 🎉")
    else:
        print(f"{failed} test(s) failed.")

