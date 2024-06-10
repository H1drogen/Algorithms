using NUnit.Framework;
using DefaultNamespace;

[TestFixture]
public class RotateArrayTests
{
    private RotateArray _rotateArray;

    [SetUp]
    public void Setup()
    {
        _rotateArray = new RotateArray();
    }

    [Test]
    public void TestRotate()
    {
        int[] nums = {1, 2, 3, 4, 5};
        int k = 2;
        _rotateArray.Rotate(nums, k);

        // Assert that the array has been rotated correctly
        Assert.AreEqual(new int[] {4, 5, 1, 2, 3}, nums);
    }
}